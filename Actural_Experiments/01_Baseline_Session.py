# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:15 2019

This is the baseline session for both TD and ASD kids
each practice will be judged by researcher
This session is a test session for demostrating basic sense
of how this experiment will look like

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
#import ssh
import numpy as np
import recordplay
#import stft
from naoqi import ALProxy
from scipy.io import wavfile as wav
import csv
import datetime
#import audio_generator

print "Enter kid name:\n"
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
#    postureProxy.goToPosture("Crouch", 0.4)
    Positions.userInitPosture(motionProxy, postureProxy)
    motionProxy.rest()

# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    while(True):
        
        taskNumber = int(raw_input("select task:\n\
                                   0: intro\n\
                                   1: single note play\n\
                                   2: single note with color\n\
                                   3: multiple notes with color\n\
                                   4: first half song practice\n\
                                   5: second half song practice\n\
                                   6: whole song play\n\
                                   7: take break\n\
                                   8: free play\n\
                                   9: end session\n\
                                   10: ask robot show again\n\
                                   11: well done move on next one\n\
                                   12: robot ask kid try it again\n\
                                   13: start record 5 seconds\n\
                                   14: play back\n\
                                   15: hidden harder version song play\n\
                                   16: start record 30 seconds for whole song\n\
                                   17: well done \n\
                                   18: test position ok\n\
                                   please make selection: "))
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session
            tts.say("Hello")
            tts.say(kid_name)
            time.sleep(0.5)
            tts.say("Welcome to NAO music party!")
            time.sleep(1.0)
            tts.say("Today, we are going to learn a lovely song!")
            ledProxy.randomEyes(2.0)
            tts.say("Let me show you how to play!")
            time.sleep(0.5)   
# =============================================================================
#           Play twinkle twinkle
            dt = 0.6
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]

            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            motionProxy.rest()
            ledProxy.randomEyes(2.0)
            tts.say("Do you recognize this song from somewhere?")
            time.sleep(3.0)
            tts.say("Yes, it is the the most popular Twinkle Twinkle Little Star!")
            time.sleep(3.0)
#           may use speech recognition instead of this
            tts.say("Do you like it?")
            time.sleep(3.0)
            tts.say("Let's start our practice!")
            tts.say("You may find a pair of red head mallet \
                    on the table somewhere.")
            time.sleep(1.0)
            tts.say("I want you to pick them up, \
                    and get ready to play following my instruction.")
#            if int(raw_input("1 for play new song, 2 for no:")):
#                
#                tts.say("Great! Let me tell you how to play this song")
            
# =============================================================================
# =============================================================================
#       task 1: Start single note play without color
        elif taskNumber == 1:
            
            keys = [0,0,1]
            dt = 0.6
            name = 'FaceLeds'
            colorName1 = 'green'
            duration = 0.5
            tts.say("Welcome to single strike challenge!")

            ledProxy.fadeRGB(name, colorName1, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
            tts.say("I just played a note, can you repeat that note for me?")
            time.sleep(1.0)
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
        
# =============================================================================
#       task 2: Start single note play along with color  
        elif taskNumber == 2: 
            
            keys = [0,0,6]
            dt = 0.6

            name = 'FaceLeds'
            colorName2 = 'blue'
            duration = 0.5
            
            tts.say("Welcome to the color challenge!")
            ledProxy.fadeRGB(name, colorName2, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy) 
            motionProxy.rest()
            tts.say("This is a new note, can you repeat that note for me?")
            time.sleep(5.0)
            tts.say("Have you notice that my eye color matchs the note color?")
            time.sleep(5.0)
            tts.say("Let's try it again, I am going to hit the blue bar now, \
                    listen carefully!")
            ledProxy.fadeRGB(name, colorName2, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
            tts.say("Now, it is your turn to play the blue bar!")
            tts.say("And try to use your left hand to do this.")
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
        
# =============================================================================
#       task 3: Start multiple notes play along with color
        elif taskNumber == 3:
                
            keys = [0,0,1,5,6]
            dt1 = 1
            name = 'FaceLeds'
#            colorNames = ['red', 'green', 'blue']
            duration = 0.5
            
            tts.say("Welcome to the triple blend challenge!")
            ledProxy.randomEyes(2.0)
        
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            
            Positions.playXyloOne(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
            tts.say("I just played three notes, can you repeat them for me? \
                    make sure you followed by the proper color order\
                    for example green, gray, blue.")
#            tts.say("Now, if you can sing the color while hitting the note \
#                    that would be even better!")
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
        
# =============================================================================
#       task 4: Start play whole song 
#       first half song
        elif taskNumber == 4:
            
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1]
            name = 'FaceLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5
            dt1 = 1
            tts.say("Here comes the ultimate challenge!")
            tts.say("This is the first half of the song! \
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
#            tts.say("Did you get it?")
#            time.sleep(1.0)

            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
#       task 5: Start play whole song 
#       second half song 
        elif taskNumber == 5:
            
            keys = [0,0,5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0]
            dt1 = 1
            name = 'FaceLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the ultimate challenge! \
                    This is second half of the song\
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
#            tts.say("Did you get it?")
#            time.sleep(1.0)

            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))

# =============================================================================
#       task 6: play the whole song
        elif taskNumber == 6:
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
            dt=0.6
            name = 'FaceLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Final challenge! \
                    Here comes the whole song! \
                    Listen and watch carefully.")
            tts.say("I will use normal speed to play.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXyloOne(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
#            tts.say("Did you get it?")
#            time.sleep(1.0)

            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, keys, '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))

# =============================================================================
#       task 7: take a break for 180 seconds      
        elif taskNumber == 7:
            
            tts.say("Do you want to take a break?")
            tts.say(" If yes, You will have 180 seconds \
                    for a short break!")
#            tts.say("Starting now!")
#            ledProxy.randomEyes(3.0)
#            time.sleep(57)
#            tts.say("You have 120 seconds left.")
#            ledProxy.randomEyes(3.0)
#            time.sleep(57)
#            tts.say("You have one minunt left.")
#            ledProxy.randomEyes(3.0)
#            time.sleep(57)
#            tts.say("Shall we start the next task?")  
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, 'break', 'break', 'break'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
#       task 8: free play
        elif taskNumber == 8:
            
            tts.say("We are done with practice today.")
            time.sleep(1.0)
            tts.say("Feel free to create any music if you may like.")
            time.sleep(1.0)
            tts.say("If you decide to leave, please say Goodbye.")

# =============================================================================
#       task 9: end the session get out the loop
        elif taskNumber == 9:
            tts.say("Have a nice day! Hope I can see you next time!")            
            motionProxy.rest()
            break
# =============================================================================
        
#       other typo or mistakes
#        task 10: ask for help from robot
        elif taskNumber == 10:
            tts.say("It looks like you may need some help. \
                    Do you want me to show you again?")
            motionProxy.rest()
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, '0', '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
#        task 11: reward for kid    
        elif taskNumber == 11:
            tts.say("Well done! You just unlocked a new challenge, \
                    let's try it now!")
            motionProxy.rest()
# =============================================================================
#        task 12: based on bad result, ask kid try again and no NAO play    
        elif taskNumber == 12:
            tts.say("It doesn't sound quite right, \
                    please try it again. I am listening.")
            motionProxy.rest()
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([taskNumber, '0', '0', '0'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
#        task 13: record what kid plays and play back let kid confirm    
        elif taskNumber == 13:
            tts.say("You may start your play after you see my eye flashs.")
            tts.say("You will have ten seconds to play.")
            tts.say("If you need help, please say help!")
            ledProxy.randomEyes(1.0)
            tts.say("Now, start your play.")
            recordplay.record(robotIP, PORT, t=10)
            
        elif taskNumber ==14:
            dst = '/home/nao/uplay.wav'
            tts.say("This is what you just played.")
            recordplay.playBack(robotIP, PORT, dst)

            
# =============================================================================
#        task 15: shh, transfer file and ntft get frequency, then make judgement
#        send feedback to kid
        elif taskNumber == 15:
            

            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
            
            dt = 0.53

            tts.say("Looks like you just unlucked a hidden challenge! \
                    Listen and watch carefully.")
            tts.say("See if you can follow after I finished.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
            tts.say("Did you get it?")
            time.sleep(1.0)

            
# =============================================================================
        elif taskNumber == 16:
            tts.say("You may start your play after you see my eye flashs.")
            tts.say("You will have thirty seconds to play.")
            tts.say("If you need help, please say help!")
            ledProxy.randomEyes(1.0)
            tts.say("Now, start your play.")
            recordplay.record(robotIP, PORT, t=30)  
            
        elif taskNumber == 17:
            tts.say("Well done! You did really good!")
            motionProxy.rest()
            
        elif taskNumber == 18:
            
            keys = [0, 1,2,3,4,5,4,3,2,1]
            dt1 = 0.6
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.playXyloOne(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            motionProxy.rest()
            
        else:
            continue
        
# =============================================================================
# Calling the main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
#    parser.add_argument("--ip", type=str, default="127.0.0.1",
#                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
#    parser.add_argument("--port", type=int, default=53337,
#                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program