# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:18:05 2019

This function is for help child to play xylophone properly
that can help robot better recognize notes at some point
and this is also can be consider as a motor control practice
robot will provide same contant to both groups and will see
different learning curve between two groups of kids

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
import speechrecognition

# before run this, make sure the IP is currect
global broker; broker = ALBroker("pythonBroker","0.0.0.0", 0, "192.168.0.2", 9559)
global pythonSpeechModule; pythonSpeechModule = speechrecognition.SpeechRecoModule('pythonSpeechModule')

print "Enter subject Name:\n"
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

fileName = subject + '_' + session  + '_' + 'hit_practice_' + mon + '_' + day + '_' + year + '.csv'

try:
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['number of practice', 'ground_truth', 'kid_input', 'result', 'number ask for help'])
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
    
def createMisc(robotIP, username, pw):
    
    play_note = []
    newData = []
    uncfList = ['1','2','3','4','5','6','7','8','9','10','11']
    comfList = ['1','2','3','4','5','6','7','8','9','10','11']

    mode = ['u', 'c']
    u_cList = random.choice(mode)
    n = 1
    if u_cList == 'u':
        for i in range(n):
            play_note.append(random.choice(uncfList))
    else:
        for i in range(n):
            play_note.append(random.choice(comfList))
    print(play_note)
    
    for j in play_note:
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
    
    return dst, play_note
    
# =============================================================================
def sampleHit(motionProxy, postureProxy, ledProxy, tts, play_note):
    
    Positions.userInitPosture(motionProxy, postureProxy)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    dt = 1.0
    Positions.playXyloOne(motionProxy, play_note, dt)
    Positions.userReadyToPlay(motionProxy, postureProxy)
    Positions.userInitPosture(motionProxy, postureProxy)
    motionProxy.rest()

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
    Positions.userInitPosture(motionProxy, postureProxy)

    motionProxy.rest()
    
    tts.say("Hello") # figure out how to say name in tts
    tts.say(kid_name)
    tts.say("Before we start our practice, I would like to help you with a 10 minutes warm up!")
    tts.say("In this warm up section, I will ask you to play some notes.")
    tts.say("And I want you to follow my instruction carefully.")
    tts.say("You will play a single note after my eye flashs!")
    tts.say("Try to make it sounds like what you just heard.")
    tts.say("I am waiting a clear and long lasting sound!")
    tts.say("Let's begin!")
    
    count = 0.0
    result = 0.0 
    good = 1
    bad = 0
    color = 'nothing'
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    while(True):
        
        help_count = 100
        
        if count < 10:
            
            dst, play_note = createMisc(robotIP, username, pw)
            print('creat music done!')
            tts.say("Here is what I want you to play now, listen carefully!")
            recordplay.playBack(robotIP, PORT, dst)
            time.sleep(3)
            print('playback ok!')
            
            if play_note[0] == '1' or play_note[0] == '8':
                color = 'green'
            elif play_note[0] == '2' or play_note[0] == '9':
                color = 'brown'
            elif play_note[0] == '3' or play_note[0] == '10':
                color = 'red'
            elif play_note[0] == '4' or play_note[0] == '11':
                color = 'yellow'
            elif play_note[0] == '5':
                color = 'gray'
            elif play_note[0] == '6':
                color = 'blue'
            else:
                color = 'pink'
            
            tts.say("Now, so I just played")
            tts.say(color)
            tts.say("It is your turn to play now!")
                
            tts.say("After you see my eyes flash, you may start to play!")
        
            ledProxy.randomEyes(1.0)
            tts.say("Now, play")
            tts.say(color)
            recordplay.record(robotIP, PORT, t=3)
            print("record done!")
            
            origin = '/home/nao/uplay.wav'
            dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Actural_Experiments\uplay.wav'
            
            sshFile = ssh.SSHConnection (robotIP, username, pw)
            sshFile.get(origin, dst)
            sshFile.close()
            print("file download complete!")
               
            sampleRate, data = wav.read(dst)
        #        N = len(data)
            Nwin = 2048
            xx = data[:, 0]
                    
            low = 1040
            high = 2800
            x = stft.bandpass_filter(xx, low, high, sampleRate, order=3)
        
            s = np.abs(stft.stft(x, Nwin))
            
            peaks = stft.findNotes(s, sampleRate/2)
            realPeaks = stft.realPeak(peaks)
            print("audio analysis done! here is the note detected: ")
            print(realPeaks)
            if len(realPeaks) == 0:
                
                count += 1      # test see if count will change in here
                result = bad
                responseList = ["Looks like you didn't play it very well.",
                                "Sorry, I couldn't recognize it.",
                                "Sorry, I didn't get that one.",
                                "I think you might missed it.",
                                "That was not a perfect one, but it is OK."]
                response = random.choice(responseList)
                tts.say(response)

                tts.say("Do you want me to show you a good strike?")
                tts.say("Or we can move on to the next one.")
                tts.say("You can say yes or no after the beep.")
                
                pythonSpeechModule.onLoad()
                pythonSpeechModule.onInput_onStart()
                time.sleep(5)
                pythonSpeechModule.onUnload()
                
                if pythonSpeechModule.targetWord == '<...> yes <...>':
                    tts.say("Let me tell you a key to achieve a perfect strike!")
                    tts.say("Before you hit, you may want to relax your wrist.")
                    tts.say("And then, you strike the bar quickly do this move.")
                    tts.say("Down and Up!")
                    time.sleep(0.5)
                    tts.say("I believe there will be a perfect sound after that strike.")
                    tts.say("OK, now let me show you how to hit the bar properly!")
                    tts.say("Listen and watch carefully!")
                    keys = convertKeys(play_note) 
                    print(keys)
                    sampleHit(motionProxy, postureProxy, ledProxy, tts, keys)
                    tts.say("Did you get it? Let's try another one. Follow my instructions.")
                    help_count = 1
                    
                elif pythonSpeechModule.targetWord == '<...> no <...>':
                    tts.say("OK, we can play the next note.")
                    help_count = 0     
                    
                else:
                    tts.say("OK, let's just move on to the next note.")
                    help_count = 2
                
                pythonSpeechModule.reset()
                
                try:
                    with open(fileName, 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', 
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow([count, play_note, realPeaks[0], result, help_count])
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
                               
            else:
                count += 1
                result = good
                responseList = ["Well done! You find the correct color and played very well!",
                                "Awesome! Keep this feeling! Let's try another one!",
                                "Great! Here comes the next one!",
                                "You are doing great! Ready for the next one!",
                                "Nice job! Let's focus on the next one!"]
                response = random.choice(responseList)
                tts.say(response)
                
                try:
                    with open(fileName, 'a') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', 
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow([count, play_note, realPeaks[0], result, help_count])
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
                    
        else:
            tts.say("Congratulations! You just completed the warm up practice!")
            break
        
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