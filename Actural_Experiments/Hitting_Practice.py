# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:18:05 2019

@author: CV_LAB_Howard
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
from naoqi import ALBroker
from scipy.io import wavfile as wav
import csv
import datetime
import random
import os
import copy

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
fileName = subject + '_' + session  + '_' + 'hit_practice_' + year + '_' + mon + '_' + day + '.csv'

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
    n = 16
    if u_cList == 'u':
        for i in range(n):
            play.append(random.choice(uncfList))
    else:
        for i in range(n):
            play.append(random.choice(comfList))
    print(play)
    
    for j in play:
        rate, data = wav.read(j + '.wav')
        if len(newData) == 0:
            newData = copy.deepcopy(data)
        else:
            newData = np.concatenate((newData, data), axis=0)
#    print('music creating done')
    newFile = 'imitate_' + u_cList +  '.wav'
    wav.write(newFile, rate, newData)
#    print('music write to folder done')
        
    dst = '/home/nao/' + newFile
    # this path need to be changed
    origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Actural_Experiments', newFile)
    sshFile = ssh.SSHConnection(robotIP, username, pw)
    print('connection ok')
    sshFile.put(origin, dst)
    sshFile.close()
    
    return dst, play
    
# =============================================================================
def game2(robotIP, PORT, username, pw, origin, local, motionProxy, postureProxy, ledProxy, tts):
    tts.say("In this mode, you will have five seconds to play what ever you want.")
    tts.say("When times up, I will try to mimic what I heard from you.")
    tts.say("After you see my eyes flash, you may start to play! Try to hit harder!")
    ledProxy.randomEyes(1.0)
    recordplay.record(robotIP, PORT, t=5)
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

    s = np.abs(stft.stft(x, Nwin))
    
    peaks = stft.findNotes(s, sampleRate/2)
    realPeaks = stft.realPeak(peaks)
    print(realPeaks)
    dt = 0.6
    orgKeys = realPeaks
    keys = convertKeys(orgKeys)
    tts.say("I think I got it!")
    tts.say("Now it is my turn to play!")
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.playXyloOne(motionProxy, keys, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.userInitPosture(motionProxy, postureProxy)
    motionProxy.rest()
    tts.say("It was an easy one! How do you rate my performance? From zero to ten!")
    ledProxy.randomEyes(2.0)
    time.sleep(3)
    tts.say("Thanks for playing this game, which game do you want to play next?")
    tts.say("You may also say exit to quit play with me!")
    

def convertKeys(keys):
    trueKeys = []
    trueKeys.append(0)
    trueKeys.append(0)
    for i in range(len(keys)):
        if keys[i] == '1':
            trueKeys.append(1)
            continue
        elif keys[i] == '2':
            trueKeys.append(2)
            continue
        elif keys[i] == '3':
            trueKeys.append(3)
            continue
        elif keys[i] == '4':
            trueKeys.append(4)
            continue
        elif keys[i] == '5':
            trueKeys.append(5)
            continue
        elif keys[i] == '6':
            trueKeys.append(6)
            continue
        elif keys[i] == '7':
            trueKeys.append(7)
            continue
        elif keys[i] == '8':
            trueKeys.append(8)
            continue
        elif keys[i] == '9':
            trueKeys.append(9)
            continue
        elif keys[i] == '10':
            trueKeys.append(10)
            continue
        else:
            trueKeys.append(11)
            continue
            
    return trueKeys
    
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
#    postureProxy.goToPosture("Crouch", 0.4)
    Positions.userInitPosture(motionProxy, postureProxy)

    motionProxy.rest()

# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    while(True):
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session

# =============================================================================

#        game 1    
        if taskNumber == 1:
            
            game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy, tts)
            pythonSpeechModule.onLoad()
            pythonSpeechModule.onInput_onStart()
            time.sleep(5)
            pythonSpeechModule.onUnload()
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, '0', '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
#       game 2
        elif taskNumber == 2:
        

            origin = '/home/nao/uplay.wav'
            dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\uplay.wav'
            game2(robotIP, PORT, username, pw, origin, dst, motionProxy, postureProxy, ledProxy, tts)
            pythonSpeechModule.onLoad()
            pythonSpeechModule.onInput_onStart()
            time.sleep(5)
            pythonSpeechModule.onUnload()
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, '0', '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))

# =============================================================================
        elif taskNumber == 3:
            break
        
        else:
            continue
        
# =============================================================================
# Calling the main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.3",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program