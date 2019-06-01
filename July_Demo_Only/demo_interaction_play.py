# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:43:08 2019

@author: Howard
"""

# =============================================================================
# This is a find notes and hit template 
# =============================================================================
#import almath
import time
import sys
import argparse
#import motion
import Positions
import ssh
import numpy as np
import recordplay
import stft
from naoqi import ALProxy
from scipy.io import wavfile as wav
import csv
import datetime
import random
import os
import copy
#import audio_generator

songBank = {"Twinkle": [0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                        5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                        1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0], 

            "QingHuaCi": [0,2,1,6,1,0,1,6,1,0,1,6,1,6,5,0,0,2,1,6,1,0,1,6,1,0,
                          1,3,2,1,1,0,0,5,6,3,3,0,3,2,3,0,3,2,3,5,0,3,0,3,3,3,
                          2,2,2,2,2,0,1,3,0,0,0,0,0,2,1,6,1,0,1,6,1,0,1,6,1,6,
                          5,0,0,5,6,3,5,0,5,3,5,0,5,3,2,1,1,0,0,2,1,2,3,2,2,0,
                          2,0,1,6,2,1,1,6,1,0,1,1,0,0,0,0,0,0,0,0,4,0,3,0,2,5,
                          5,3,2,3,4,0,2,3,5,3,2,0,0,0,0,5,5,3,2,3,5,0,2,3,5,2,
                          1,0,0,0,0,1,2,3,5,6,5,4,5,3,3,2,2,0,0,0,0,1,2,1,1,0,
                          1,2,0,3,0,5,0,3,0,0,0,5,5,3,2,3,6,0,2,3,5,3,2,0,0,0,
                          0,5,5,3,2,3,5,0,2,3,5,2,1,0,0,0,0,1,2,3,5,6,5,4,5,3,
                          3,2,2,0,0,5,3,0,2,2,0,1,0,0],
                          
            "Promise": [0,6,7,8,9,10,9,8,7,6,0,3,0,6,0,
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,0,
                        0,6,7,8,9,10,9,8,7,6,0,3,0,6,0,
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,0]}


print "Enter subject number:\n"
subject = raw_input()
print "Enter session number:\n"
session = raw_input()
now = datetime.datetime.now()
day = str(now.day)
mon = str(now.month)
year = str(now.year)
task = 0
username = "nao"
pw = "nao"
fileName = subject + '_' + session  + '_' + year + '_' + mon + '_' + day + '.csv'

try:
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['task', 'ground_truth', 'kid_input', 'result'])
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# 
    
def createMisc(robotIP, username, pw):
    
    play = []
    newData = []
    uncfList = ['3','4','7','8','10','11']
    comfList = ['1','2','4','5','6','8','9']
    mode = ['u', 'c']
    u_cList = random.choice(mode)
    n = 6
    if u_cList == 'u':
        for i in range(n):
            play.append(random.choice(uncfList))
    else:
        for i in range(n):
            play.append(random.choice(comfList))
    print(uncfList, comfList, play)
    
    for j in play:
        rate, data = wav.read(j + '.wav')
        if len(newData) == 0:
            newData = copy.deepcopy(data)
        else:
            newData = np.concatenate((newData, data), axis=0)
    
    newFile = 'imitate' + u_cList +  '.wav'
    wav.write(newFile, rate, newData)
        
    dst = '/home/nao/' + newFile
    # this path need to be changed
    origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
    sshFile = ssh.SSHConnection(robotIP, username, pw)
    sshFile.put(origin, dst)
    sshFile.close()
    
    return dst, play
    
def game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy):
    dst, play = createMisc();
    recordplay.playBack(robotIP, PORT, dst)
    print(play)
    dt = 0.6
    keys = play
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.playXylo(motionProxy, keys, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.userInitPosture(motionProxy, postureProxy)
    ledProxy.randomEyes(2.0)
    motionProxy.rest()

    
# =============================================================================
def game2(robotIP, PORT, username, pw, origin, local, motionProxy, postureProxy, ledProxy):
    recordplay.record(robotIP, PORT, t=10)
#        recordplay.playBack(robotIP, PORT)

    sshFile = ssh.SSHConnection (robotIP, username, pw)
    sshFile.get(origin, local)
    sshFile.close()
       
    sampleRate, data = wav.read(local)
#        N = len(data)
    Nwin = 2048
    xx = data[:, 0]
            
    low = 1040
    high = 2800
    x = stft.bandpass_filter(xx, low, high, sampleRate, order=3)
            # Generate a chirp: start frequency at 5 Hz and going down at 2 Hz/s
#        totleTime = np.arange(N) / sampleRate  # seconds
        #    x = np.cos(2 * np.pi * time * (5 - 2 * 0.5 * time))
        
            # Test with Nfft bigger than Nwin
#        Nfft = Nwin * 2
    s = np.abs(stft.stft(x, Nwin))
#        y = stft.istft(s, Nwin)
    peaks = stft.findNotes(s, sampleRate/2)
    realPeaks = stft.realPeak(peaks)
    dt = 0.6
    keys = realPeaks
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.playXylo(motionProxy, keys, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.userInitPosture(motionProxy, postureProxy)
    ledProxy.randomEyes(2.0)
    motionProxy.rest()
    

    
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy.goToPosture("Crouch", 0.4)
#    asr = ALProxy("ALSpeechRecognition", robotIP, PORT)
    Positions.userInitPosture(motionProxy, postureProxy)
#    asr.setLanguage("English")
#    menu = ["menu list"]
#    menuList = ["shuffle play", "copy me", "teach me"]
#    pstvAnsList = ["yes", "ok", "good", "go for it"]
#    ngtvAnsList = ["no", "not", "don't", "stop"]
    motionProxy.rest()
    tts.say("Hello, there!")
    time.sleep(0.5)
    tts.say("Welcome back to NAO music party!")
    time.sleep(1.0)
    tts.say("Let me show you my talent!")
    ledProxy.randomEyes(2.0)
    tts.say("Tell me which mode do you want to try?")
    time.sleep(1.0)
    tts.say("You can say show menu list to know the options.")
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    for i in range(1000):
        
        taskNumber = int(raw_input("select task:\n\
                                   0: Demo a song\n\
                                   1: I play you play\n\
                                   2: you play I play\n\
                                   please make selection: "))

#        asr.setVocalbulary(menu, False)
        
        
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session


# =============================================================================
#           Play twinkle twinkle
            dt = 0.6
            keys = songBank["Promise"]

            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            motionProxy.rest()

        
# =============================================================================

#        task 13: record what kid plays and play back let kid confirm    
        elif taskNumber == 1:
            
            game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy)
# =============================================================================
#        task 14: shh, transfer file and ntft get frequency, then make judgement
#        send feedback to kid
        elif taskNumber == 2:
        

            origin = '/home/nao/test.wav'
            dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source\test.wav'
            game2(robotIP, PORT, username, pw, origin, dst, motionProxy, postureProxy, ledProxy)

# =============================================================================
            
        else:
            continue
        
# =============================================================================
# Calling the main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program