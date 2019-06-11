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

#            "QingHuaCi": [0,2,1,6,1,0,1,6,1,0,1,6,1,6,5,0,0,2,1,6,1,0,1,6,1,0,
#                          1,3,2,1,1,0,0,5,6,3,3,0,3,2,3,0,3,2,3,5,0,3,0,3,3,3,
#                          2,2,2,2,2,0,1,3,0,0,0,0,0,2,1,6,1,0,1,6,1,0,1,6,1,6,
#                          5,0,0,5,6,3,5,0,5,3,5,0,5,3,2,1,1,0,0,2,1,2,3,2,2,0,
#                          2,0,1,6,2,1,1,6,1,0,1,1,0,0,0,0,0,0,0,0,4,0,3,0,2,5,
#                          5,3,2,3,4,0,2,3,5,3,2,0,0,0,0,5,5,3,2,3,5,0,2,3,5,2,
#                          1,0,0,0,0,1,2,3,5,6,5,4,5,3,3,2,2,0,0,0,0,1,2,1,1,0,
#                          1,2,0,3,0,5,0,3,0,0,0,5,5,3,2,3,6,0,2,3,5,3,2,0,0,0,
#                          0,5,5,3,2,3,5,0,2,3,5,2,1,0,0,0,0,1,2,3,5,6,5,4,5,3,
#                          3,2,2,0,0,5,3,0,2,2,0,1,0,0],
                          
            "Promise": [0,6,7,8,9,10,9,8,7,6,0,3,0,6,0,
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,
                        0,6,7,8,9,10,9,8,7,6,0,3,0,6,0,
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6]}


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
    n = 8
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
    origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\July_Demo_Only', newFile)
    sshFile = ssh.SSHConnection(robotIP, username, pw)
    print('connection ok')
    sshFile.put(origin, dst)
    sshFile.close()
    
    return dst, play
    
def game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy, tts):
    dst, play = createMisc(robotIP, username, pw)
    print('creat music done')
    tts.say("Here is what I will play now, listen carefully!")
    recordplay.playBack(robotIP, PORT, dst)
    time.sleep(6)
    print('playback ok')
    dt = 0.8
    orgKeys = play
    keys = convertKeys(orgKeys)
    tts.say("This is how I play, watch carefully!")
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.playXyloOne(motionProxy, keys, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    tts.say("Now it is your time to play! You have ten seconds to play.")
    Positions.userInitPosture(motionProxy, postureProxy)
    tts.say("When you see my eyes flash, you may start.")
    ledProxy.randomEyes(2.0)
    motionProxy.rest()
    time.sleep(10)
    tts.say("Times up! You did really well! Which mode you want to play next?")
    tts.say("You may also say exit to quit play with me!")

    
# =============================================================================
def game2(robotIP, PORT, username, pw, origin, local, motionProxy, postureProxy, ledProxy, tts):
    tts.say("In this mode, you will have five seconds to play what ever you want.")
    tts.say("When times up, I will try to mimic what I heard from you.")
    tts.say("After you see my eyes flash, you may start to play!")
    ledProxy.randomEyes(2.0)
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
    tts.say("Hello there!")
    time.sleep(0.5)
    tts.say("Welcome back to NAO music party!")
    time.sleep(1.0)
    tts.say("Let me show you my talent!")
    ledProxy.randomEyes(2.0)
    tts.say("Tell me which mode do you want to try?")
    tts.say("You can say Demo, Mimic Practice or Free Play.")
    time.sleep(1.0)
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    for i in range(1000):
        
        taskNumber = int(raw_input("select task:\n\
                                   0: Demo a song\n\
                                   1: game 1\n\
                                   2: game 2\n\
                                   please make selection: "))

# =============================================================================
        if taskNumber == 0:
#           Intro to entire session

# =============================================================================
#           Play demo
            dt = 0.4
            keys = songBank["Promise"]

            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            motionProxy.rest()
            tts.say("Thanks for listening! Which mode you want to play next?")
            tts.say("You may also say exit to quit play with me!")
        
# =============================================================================

#        game 1    
        elif taskNumber == 1:
            
            game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy, tts)
# =============================================================================
#       game 2
        elif taskNumber == 2:
        

            origin = '/home/nao/uplay.wav'
            dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\July_Demo_Only\uplay.wav'
            game2(robotIP, PORT, username, pw, origin, dst, motionProxy, postureProxy, ledProxy, tts)

# =============================================================================
            
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