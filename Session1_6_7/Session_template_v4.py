# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:15 2019

@author: CV_LAB_Howard
"""
# =============================================================================
# This is a find notes and hit template 
# =============================================================================
import almath
import time
import argparse
import motion
import Positions
from naoqi import ALProxy


# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy.goToPosture("Crouch", 0.4)
    Positions.userInitPosture(motionProxy, postureProxy)
    motionProxy.rest()
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    for i in range(1000):
        
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
                                   please make selection: "))
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session
            tts.say("Hello, Seena!")
            time.sleep(0.5)
            tts.say("Welcome back to NAO music party!")
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

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            tts.say("Do you recognize this song from somewhere?")
            time.sleep(5.0)
            tts.say("Yes, it is the the most popular Twinkle Twinkle Little Star!")
            time.sleep(3.0)
#           may use speech recognition instead of this
            tts.say("Do you like it?")
            time.sleep(5.0)
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
            duration = 1.0
            tts.say("Welcome to the strike challenge!")

            ledProxy.fadeRGB(name, colorName1, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            tts.say("I just played a note, can you repeat that note for me?")
            time.sleep(1.0)

        
# =============================================================================
#       task 2: Start single note play along with color  
        elif taskNumber == 2: 
            
            keys = [0,0,6]
            dt = 0.6

            name = 'FaceLeds'
            colorName2 = 'blue'
            duration = 1.0
            
            tts.say("Welcome to the color challenge!")
            ledProxy.fadeRGB(name, colorName2, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)    
            tts.say("This is a new note, can you repeat that note for me?")
            time.sleep(5.0)
            tts.say("Have you notice that my eye color matchs the note color?")
            time.sleep(5.0)
            tts.say("Let's try it again, I am going to hit the blue bar now, \
                    listen carefully!")
            ledProxy.fadeRGB(name, colorName2, duration)
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            tts.say("Now, it is your turn to play the green bar!")
            tts.say("And try to use your left hand to do this.")

        
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
            
            Positions.playXylo(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
            tts.say("I just played three notes, can you repeat them for me? \
                    make sure you followed by the proper color order\
                    for example green, gray, blue.")
            time.sleep(5.0)
#            tts.say("Now, if you can sing the color while hitting the note \
#                    that would be even better!")

        
# =============================================================================
#       task 4: Start play whole song 
#       first half song
        elif taskNumber == 4:
            
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1]
            name = 'FacdLeds'
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

            Positions.playXylo(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
#            tts.say("Did you get it?")
#            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")
            tts.say("If you need help, please say Help.")

# =============================================================================
#       task 5: Start play whole song 
#       second half song 
        elif taskNumber == 5:
            
            keys = [0,0,5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0]
            dt1 = 1
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the ultimate challenge! \
                    This is second half of the song\
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt1)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
#            tts.say("Did you get it?")
#            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")
            tts.say("If you need help, please say Help.")


# =============================================================================
#       task 6: play the whole song
        elif taskNumber == 6:
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
            dt=0.6
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Final challenge! \
                    Here comes the whole song! \
                    Listen and watch carefully.")
            tts.say("I will use normal speed to play.")
            Positions.userInitPosture(motionProxy, postureProxy)
            Positions.userReadyToPlay(motionProxy, postureProxy)

            Positions.playXylo(motionProxy, keys, dt)
            Positions.userReadyToPlay(motionProxy, postureProxy)
            Positions.userInitPosture(motionProxy,postureProxy)
#            tts.say("Did you get it?")
#            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")
            tts.say("If you need help, please say Help.")


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
        
# =============================================================================
#       task 8: free play
        elif taskNumber == 8:
            
            tts.say("We are done with practice today.")
            time.sleep(1.0)
            tts.say("Feel free to stay and play whatever song you may like.")
            time.sleep(1.0)
            tts.say("If you decide to leave, please say Goodbye to me.")

# =============================================================================
#       task 9: end the session get out the loop
        elif taskNumber == 9:
            tts.say("Have a nice day! See you next time!")            
            motionProxy.rest()
            break
        
#       other typo or mistakes
            
        elif taskNumber == 10:
            tts.say("It looks like you may need some help. \
                    Do you want me to show you again?")
            motionProxy.rest()
            
        elif taskNumber == 11:
            tts.say("Well done! You just unlocked a new challenge, \
                    let's try it now!")
            motionProxy.rest()
            
        elif taskNumber == 12:
            tts.say("It doesn't sound quite right, \
                    please try it again. I am listening.")
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

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program