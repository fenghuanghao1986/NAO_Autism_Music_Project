# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 12:52:25 2019

02_Single_Note_Practice_Session

@author: CV_LAB_Howard
"""

# =============================================================================

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

username = "nao"
pw = "nao"

fileName = subject + '_' + session  + '_' + 'single_note_practice_' + mon + '_' + day + '_' + year + '.csv'

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
    uncfList = ['1','2','3','4','5','6','7','8','9','a','b']
    comfList = ['1','2','3','4','5','6','7','8','9','a','b']
#    uncfList = ['8','8','8','8']
#    comfList = ['7','7','7']
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
    Positions.userInitPosture(motionProxy, postureProxy)

    motionProxy.rest()
    
    tts.say("Hello") # figure out how to say name in tts
    tts.say(kid_name)
    tts.say("Welcome to the single color challenge!")
    tts.say("In this challenge, I will ask you to play some single notes along with color.")
    tts.say("And I want you to follow my instruction carefully. And try to find the correct colors!")
    tts.say("You will play those notes after my eye flashs, every time!")
    tts.say("And I will tell you how well you played!")
    tts.say("I am very sensitive to sound.")
    tts.say("So it would be good for you to play it nicely. Thank you!")
    tts.say("And one more thing I may have to remind you, hopefully you have already noticed.")
    tts.say("On this xylophone, the longer the bar, the lower the pitch. And keep this in mind.")
    tts.say("You may use this in the following practice!")
    time.sleep(1.0)
    tts.say("Let's begin!")
    time.sleep(1.0)
    tts.say("Let's begin!")
    
    count = 0.0
    good = 0.0
    total = 10.0
    result = 0 
    accuracy = 0.0
    color = 'nothing'
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    while(True):
        
        help_count = 100
            
        dst, play_note = createMisc(robotIP, username, pw)
        print('creat music done!')
        tts.say("Here is what I want you to play now, listen carefully!")
        recordplay.playBack(robotIP, PORT, dst)
        time.sleep(3)
        print('playback ok!')
        
        if play_note[0] == '1' or play_note[0] == '8':
            color = 'green'
            ledProxy.fadeRGB('FaceLeds', color, 3)
        elif play_note[0] == '2' or play_note[0] == '9':
            color = 'brown'
            ledProxy.fadeRGB('FaceLeds', 0X008B4513, 3)
        elif play_note[0] == '3' or play_note[0] == 'a':
            color = 'red'
            ledProxy.fadeRGB('FaceLeds', color, 3)
        elif play_note[0] == '4' or play_note[0] == 'b':
            color = 'yellow'
            ledProxy.fadeRGB('FaceLeds', color, 3)
        elif play_note[0] == '5':
            color = 'gray'
            ledProxy.fadeRGB('FaceLeds', 0X00DCDCDC, 3)
        elif play_note[0] == '6':
            color = 'blue'
            ledProxy.fadeRGB('FaceLeds', color, 3)
        else:
            color = 'pink'
            ledProxy.fadeRGB('FaceLeds', 'magenta', 3)
            
        tts.say("Now, so I just played")
        tts.say(color)
        tts.say("Look at my eyes, they are showing ")
        tts.say(color)
        tts.say("Now, I want you to find the color and play it!")
        time.sleep(1.0)
    
        ledProxy.randomEyes(1.0)
        tts.say("Now, play ")
        tts.say(color)
        recordplay.record(robotIP, PORT, t=5)
        print("record done!")
        
        origin = '/home/nao/uplay.wav'
        dst = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Actural_Experiments\uplay.wav'
        
        sshFile = ssh.SSHConnection (robotIP, username, pw)
        sshFile.get(origin, dst)
        sshFile.close()
        print("file download complete!")
        
        sampleRate, data = wav.read(dst)
        #       N = len(data)
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
            realPeaks.append('0')
#           keys = convertKeys(realPeaks) 
        print("This is the note use for compare: ")
        print(realPeaks[0])
        
        result = stft.LevDist2(realPeaks[0], play_note)
        print("difference calculated done! Here is the result: ")
        print(result)             
    
        if result > 0:
                # call help function
            count += 1     
                
            responseList = ["Looks like you didn't play it very well.",
                            "Sorry, I couldn't recognize it.",
                            "Sorry, I didn't get that one.",
                            "I think you might missed it.",
                            "That was not a perfect one, but it is OK.",
                            "I believe you find the color! But didn't play it very well!",
                            "The color looks fine, but I couldn't recognize the notes by listening."]
            response = random.choice(responseList)
            tts.say(response)
            
            time.sleep(1.0)
            tts.say("Do you want me to show you a good strike?")
            tts.say("Or we can move on to the next one.")
            tts.say("You can say yes or no after the beep.")
            
            pythonSpeechModule.onLoad()
            pythonSpeechModule.onInput_onStart()
            time.sleep(5)
            pythonSpeechModule.onUnload()
            
            if pythonSpeechModule.targetWord == '<...> yes <...>':
                tts.say("OK, here is the correct color I want you to play!")
                tts.say("Listen and watch carefully!")
                keys = convertKeys(play_note) 
                print(keys)
                sampleHit(motionProxy, postureProxy, ledProxy, tts, keys)
                tts.say("Do you get it? Let's try another one. Follow my instructions.")
                help_count = 1
            elif pythonSpeechModule.targetWord == '<...> no <...>':
                tts.say("OK, we can try the next color.")
                help_count = 0              
            else:
                tts.say("I didn't get that, let's just move on to the next note.")
                
            pythonSpeechModule.reset()
                
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([count, play_note, realPeaks[0], result, help_count])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))  
                
        else:
                # continue the loop and run next note
            count += 1
            good += 1
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
        print("conut value: ")
        print(count)
        
        accuracy = good / count
        print("accuracy value: ")
        print(accuracy)
        
        if count < total:
            continue
        else:
            if total < 20 and accuracy < 0.5:
                total += 2
                continue
            elif total < 20 and accuracy < 0.6:
                total += 1
                continue
            elif total < 20 and accuracy >= 0.7:
                tts.say("Congratulations! You just completed single color challenge!")
                break
            else:
                tts.say("Congratulations! You just completed single color challenge!")
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