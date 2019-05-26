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
fileName = subject + '_' + session  + '_' + year + '_' + mon + '_' + day + '.csv'

try:
    with open(fileName, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['task', 'ground_truth', 'kid_input', 'result'])
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy.goToPosture("Crouch", 0.4)
    asr = ALProxy("ALSpeechRecognition", robotIP, PORT)
    Positions.userInitPosture(motionProxy, postureProxy)
    asr.setLanguage("English")
    menu = ["menu list"]
    menuList = ["shuffle play", "copy me", "teach me"]
    pstvAnsList = ["yes", "ok", "good", "go for it"]
    ngtvAnsList = ["no", "not", "don't", "stop"]
    motionProxy.rest()
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    for i in range(1000):
        
        taskNumber = int(raw_input("select task:\n\
                                   0: intro\n\
                                   1: Demo a song\n\
                                   2: I play you play\n\
                                   3: you play I play\n\
                                   please make selection: "))
        tts.say("Hello, there!")
        time.sleep(0.5)
        tts.say("Welcome back to NAO music party!")
        time.sleep(1.0)
        tts.say("Let me show you my talent!")
        ledProxy.randomEyes(2.0)
        tts.say("Tell me which mode do you want to try?")
        time.sleep(1.0)
        tts.say("You can say show menu list to know the options.")
        asr.setVocalbulary(menu, False)
        
        
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session


# =============================================================================
#           Play twinkle twinkle
            dt = 0.6
            keys = songBank["QingHuaCi"]

            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
        
# =============================================================================

#        task 13: record what kid plays and play back let kid confirm    
        elif taskNumber == 1:
            
            recordplay.record(robotIP, PORT, t=5)
            recordplay.playBack(robotIP, PORT)
# =============================================================================
#        task 14: shh, transfer file and ntft get frequency, then make judgement
#        send feedback to kid
        elif taskNumber == 2:
        
            host = "192.168.0.2"    # this host name may have to change 
            username = "nao"
            pw = "nao"
            
            origin = '/home/nao/test.wav'
            dst = r'C:\Users\fengh\Desktop\record.wav'
         
            sshFile = SSHConnection (host, username, pw)
            sshFile.get(origin, dst)
            sshFile.close()
            
        #    file = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Audio_Detection_Part\promise.wav'
            sampleRate, data = wav.read(dst)
            N = len(data)
            Nwin = 2048
            xx = data[:, 0]
            
            low = 1040
            high = 2800
            x = stft.bandpass_filter(xx, low, high, sampleRate, order=3)
            # Generate a chirp: start frequency at 5 Hz and going down at 2 Hz/s
            totleTime = np.arange(N) / sampleRate  # seconds
        #    x = np.cos(2 * np.pi * time * (5 - 2 * 0.5 * time))
        
            # Test with Nfft bigger than Nwin
            Nfft = Nwin * 2
            s = np.abs(stft.stft(x, Nwin))
            y = stft.istft(s, Nwin)
            peaks = stft.findNotes(s, sampleRate/2)
            realPeaks = stft.realPeak(peaks)
            start = time.time()
#    realPeaks = ['6', '7', '8', '9', '10', '9', '8', '6', '3', '6', '7', '8', '9', '8', '7', '6', '8', '7', '6', '5', '7']
            r_len = len(realPeaks)
#            change orgpeaks to the key that nao just played or the music just played
#           find a way please!
            orgPeaks = ['6', '7', '8', '9', '10', '9', '8', '5', '3', '6', '7', '8', '9', '8', '7', '6', '8', '7', '6', '5', '7', '6']
            o_len = len(orgPeaks)
#            result = [[-1 for i in range(len(realPeaks))] for j in range(len(orgPeaks))]
        
            diff = stft.LevDist2(realPeaks, orgPeaks)
            sim = 1 - (float(diff)/(float(o_len)))
            end = time.time()
            print("stft time: " + str(end - start))
            print(diff, sim)
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, '123', '122', '.667'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
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