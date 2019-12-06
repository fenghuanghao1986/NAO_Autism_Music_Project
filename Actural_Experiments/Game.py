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
from naoqi import ALBroker
from scipy.io import wavfile as wav
import csv
import datetime
import random
import os
import copy
#import audio_generator
import speechrecognition

global broker; broker = ALBroker("pythonBroker","0.0.0.0", 0, "192.168.0.2", 9559)
global pythonSpeechModule;
pythonSpeechModule = speechrecognition.SpeechRecoModule('pythonSpeechModule')

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
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6,
                        0,6,7,8,9,10,9,8,7,6,0,3,0,6,0,
                        7,8,9,0,8,0,7,0,6,0,8,7,6,5,7,0,6],
                        
            "Sunshine": [0,0,5,1,2,3,0,3,0,0,3,2,3,1,0,1,0,
                         0,8,9,10,11,0,6,0,0,6,5,4,3,0,0,0,
                         0,8,9,10,11,0,6,0,0,6,5,4,3,0,1,0,
                         0,0,5,1,2,3,0,0,4,2,0,2,3,1,0,0,0],
            
            "BabySharkv1":[0,5,6,8,8,8,8,8,8,
                           0,5,6,8,8,8,8,8,8,
                           0,5,6,8,8,8,8,8,8,7],
            
            "BabySharkv2":[0,1,2,4,4,4,4,4,4,
                           0,1,2,4,4,4,4,4,4,
                           0,1,2,4,4,4,4,4,4,3],
            
            "BabySharkv3":[0,8,9,11,11,11,11,11,11,
                           0,8,9,11,11,11,11,11,11,
                           0,8,9,11,11,11,11,11,11,10],
            
            "JingleBell":[0,0,2,2,7,6,5,2,0,0,2,2,7,6,5,3,0,0,
                          3,3,8,7,6,9,9,9,9,10,9,8,6,5,0,0,
                          7,7,7,0,7,7,7,0,7,9,5,6,7,0,
                          8,8,8,8,8,7,7,7,7,6,6,7,6,0,9,0,
                          7,7,7,0,7,7,7,0,7,9,5,6,7,0,
                          8,8,8,8,8,7,7,7,9,9,8,6,5],
                          
            "Lamb": [0,0,3,2,1,2,3,3,3,0,2,2,2,0,3,5,5,0,
                    3,2,1,2,3,3,3,1,0,2,2,3,2,1,0,8,0,
                    7,6,5,6,7,7,7,0,6,6,6,0,7,9,9,0,
                    7,6,5,6,7,7,7,7,0,6,6,7,6,5,0,9,0],
                     
            "Fatastic": [0,0,9,0,8,0,5,0,0,0,6,7,
                         8,7,6,5,4,5,6,4,5,0,7,0,2,0,6,7,
                         8,7,6,5,6,6,7,8,9,0,7,0,7,0,8,9,
                         10,0,8,0,8,0,7,6,5,0,7,0,5,0,0,0,
                         7,0,5,0,0,0,7,0,5],
                         
            "CanCan": [0,1,5,5,6,5,4,4,6,7,9,11,9,9,8,8,0,
                        9,3,3,9,8,4,4,6,6,5,6,5,6,5,6,5,
                        1,5,5,6,5,4,4,6,7,9,11,9,9,8,8,0,
                        9,3,3,9,8,4,4,6,6,5,6,5,5,4,4,0,
                        6,0,4,0,2,0,1,0,8,5,6,7,6,5,4,0,
                        6,0,4,0,2,0,1,0,7,8,9,10,5,11,11,0,
                        6,0,4,0,2,0,1,0,7,8,9,10,11,8,10,8,
                        11,8,10,8,11,8,10,8,11,8,10,8,11,8,10,8],
                       
            "Sleeping": [0,1,0,2,0,3,0,1,0,1,0,2,0,3,0,1,0,
                        3,0,4,0,5,0,0,3,0,4,0,5,0,0,
                        5,6,5,4,3,0,1,0,5,6,5,4,3,0,1,0,
                        2,0,5,0,1,0,0,2,0,5,0,1,0],
                         
            "Birds": [0,3,0,0,3,0,4,0,3,0,3,0,2,0,2,0,0,
                        6,0,6,5,0,0,0,6,6,0,5,0,6,0,4,0,
                        6,8,0,6,0,5,0,0,3,3,4,5,0,5,0,4,
                        2,0,2,0,0,3,5,0,1,0,1,0,2,0,1,0,
                        3,0,2,0,1]}

song_names = ["Fatastic", "Twinkle", "CanCan", "Sleeping", "Promise", 
              "Sunshine", "BabySharkv1", "JingleBell", "Lamb", "Birds"]

print "Enter subject name:\n"
kid_name = raw_input()
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
fileName = subject + '_' + session  + '_game_' + year + '_' + mon + '_' + day + '.csv'

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
    uncfList = ['3','4','7','8','a','b']
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
    origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Actural_Experiments', newFile)
    sshFile = ssh.SSHConnection(robotIP, username, pw)
    print('connection ok')
    sshFile.put(origin, dst)
    sshFile.close()
    
    return dst, play
    
def game1(robotIP, PORT, username, pw, motionProxy, postureProxy, ledProxy, tts):
    tts.say("In this mode, I will play some random music, and you will try to remember it and play back.")
    dst, play = createMisc(robotIP, username, pw)
    print('creat music done')
    tts.say("Here is what I will play now, listen carefully!")
    recordplay.playBack(robotIP, PORT, dst)
    time.sleep(8)
    print('playback ok')
    dt = 0.6
    orgKeys = play
    keys = convertKeys(orgKeys)
    tts.say("Before I play, let me ask you a quick question.")
    tts.say("How do you feel about what you just heard?")
    tts.say("Could you please use few words to describe it? You will have ten seconds.")
    tts.say("Thanks.")
    time.sleep(10)
    tts.say("Good to know")
    time.sleep(1)
    tts.say("This is how I play, watch carefully!")
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.playXyloOne(motionProxy, keys, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    tts.say("Now it is your time to play! You have 10 seconds to play.")
    Positions.userInitPosture(motionProxy, postureProxy)
    tts.say("When you see my eyes flash, you may start.")
    ledProxy.randomEyes(1.0)
    motionProxy.rest()
    time.sleep(10)
    tts.say("Times up!")
    responseList = [
                    "Sorry, I couldn't recognize it. Please try harder!",
                    "Sorry, I didn't get that one. You may want to try it next time.",
                    "I think you might missed some of the notes. Let's just move on.",
                    "That was not a perfect one, but it is OK. I believe you have tried your best.",
                    "I believe you find some of the colors! But not all of them!",
                    "The color looks fine, but I couldn't recognize some notes by listening.",
                    
                    "I believe you really tried, however, try it next time."]
    response = random.choice(responseList)
    tts.say(response)
    tts.say("Which mode you want to play next? You may also say exit to quit play with me!")

    
# =============================================================================
def game2(robotIP, PORT, username, pw, origin, local, motionProxy, postureProxy, ledProxy, tts):
    tts.say("In this mode, you will have five seconds to play what ever you want.")
    tts.say("When times up, I will try to mimic what I heard from you.")
    tts.say("After you see my eyes flash, you may start to play! Try to play nicely!")
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
    responseList = ["It wasn't an easy one! But I really have tried my best.",
                    "Did I just Aced it? Haha!",
                    "It was easy! You should try a harder one next time! Remember, I am a robot, I can do everything!",
                    "oops, I think I just screwed it. Can I have another chance?",
                    "That was not a perfect one, but it is OK I think. Are we on the same page?",
                    "I believe I faild you, but we are still friends, right?",
                    "I thought I got it, but all of a sudden, I got nervous, and, you know how it goes."]
    response = random.choice(responseList)
    tts.say(response)
    tts.say("How do you rate my performance? From zero to ten!")
    ledProxy.randomEyes(2.0)
    time.sleep(1)
    tts.say("Thank you!")
    tts.say("Thanks for playing this game, which game do you want to play next?")
    tts.say("You may also say exit to quit play with me!")
    
# This function is to convert str type to int type for robot to play
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
        elif keys[i] == 'a':
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
    tts.say("Hello!")
    tts.say(kid_name)
    time.sleep(0.5)
    tts.say("Welcome to NAO music game party!")
    time.sleep(1.0)
    tts.say("Let's have some fun here!")
    ledProxy.randomEyes(1.0)
    tts.say("Tell me which mode do you want to try?")
    tts.say("You can say play song, copy machine or free Play.")
    time.sleep(1.0)
    pythonSpeechModule.onLoad()
    pythonSpeechModule.onInput_onStart()
    time.sleep(5)
    pythonSpeechModule.onUnload()
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    while(True):
        
        taskNumber = 100
        if pythonSpeechModule.targetWord == '<...> free play <...>':
            taskNumber = 2
        elif pythonSpeechModule.targetWord == '<...> copy machine <...>':
            taskNumber = 1
        elif pythonSpeechModule.targetWord == '<...> play song <...>':
            taskNumber = 0
        elif pythonSpeechModule.targetWord == '<...> exit <...>':
            taskNumber = 3
        else:
            taskNumber = int(raw_input("select task:\n\
                                       0: play song\n\
                                       1: copy machine\n\
                                       2: free play\n\
                                       3: exit 3\n\
                                       please make selection: "))
        pythonSpeechModule.reset()

# =============================================================================
        if taskNumber == 0:
#           Intro to entire session

# =============================================================================
#           Play demo
            dt = 0.5
            keys = songBank[random.choice(song_names)]
#            keys = songBank["BabySharkv1"]

            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            motionProxy.rest()
            tts.say("Before we move on, let me ask you a quick question.")
            tts.say("How do you feel about what you just heard?")
            tts.say("Could you please use few words to describe it? You will have ten seconds.")
            tts.say("Thanks.")
            time.sleep(15)
            tts.say("Good to know")
            time.sleep(1)
            tts.say("Thanks for listening! Which mode you want to play next?")
            tts.say("You can say play song, copy machine or free Play.")
            tts.say("You may also say exit to quit play with me!")
            pythonSpeechModule.onLoad()
            pythonSpeechModule.onInput_onStart()
            time.sleep(5)
            pythonSpeechModule.onUnload()
        
# =============================================================================

#        game 1    
        elif taskNumber == 1:
            
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
            dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Actural_Experiments\uplay.wav'
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
            tts.say("Thanks for playing game with me!")
            break
        
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