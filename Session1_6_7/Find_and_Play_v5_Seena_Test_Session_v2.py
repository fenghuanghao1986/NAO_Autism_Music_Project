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
from naoqi import ALProxy

# =============================================================================
# these notes is for temp use, later have to save them in one file and import
# =============================================================================
notes = {}
notes = {}
# Right Arm
notes[1] = [1.2180380821228027, -0.8589081192016602, 1.514016032218933, 
             0.6151759624481201, -0.7210218906402588, 0.22]

# note 2, 3, 4, 5 may have to re-do.
notes[2] = [1.2257080078125, -0.7538580417633057, 1.5094140768051147, 
             0.6427879333496094, -0.6719338893890381, 0.22]

notes[3] = [1.2011637687683105, -0.6551759624481201, 1.5078800916671753, 
             0.7563040256500244, -0.7609059810638428, 0.22]

notes[4] = [1.2011637687683105, -0.551759624481201, 1.5078800916671753, 
             0.7563040256500244, -0.7609059810638428, 0.22]

#notes[5] = [1.1029877662658691, -0.49859189987182617, 1.501744031906128, 
#           0.84527587890625, -0.9971418380737305, 0.22]
notes[5] = [1.12755947113037, -0.45325204849243164, 1.5109480619430542, 
             0.7977218627929688, -0.8698201179504395, 0.22]
# Left Arm
notes[6] = [0.9480281066894531, 0.3328361511230469, -1.512566089630127, 
             -0.7669579982757568, 1.2271580696105957, 0.22]

notes[7] = [1.0691561698913574, 0.5491299629211426, -1.4205260276794434, 
             -0.8053081035614014, 0.9617760181427002, 0.22]

notes[8] = [1.0568840503692627, 0.6581020545959473, -1.4220600128173828, 
             -0.8252501487731934, 0.9893879890441895, 0.22]

notes[9] = [1.1075060367584229, 0.7684919834136963, -1.4650120735168457, 
             -0.7915019989013672, 0.8482601642608643, 0.22]

notes[10] = [1.3207321166992188, 0.8283181190490723, -1.679771900177002, 
             -0.8620660305023193, 0.8682019710540771, 0.22]

notes[11] = [1.3529460430145264, 0.931096076965332, -1.679771900177002, 
             -0.7500841617584229, 0.7638900279998779, 0.22]

# =============================================================================
# The following function initializes NAO's starting position or resting position
# =============================================================================
def userInitPosture(motionProxy, postureProxy):
# =============================================================================
#     # this function should have NAO crouching position with leg joints rest/locked?
#     # and both arms should be straight down without touching legs and other parts
# =============================================================================
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    names  = ["LHipYawPitch", "LHipPitch", "RHipPitch"]
    angles  = [-0.25, -0.7, -0.7]
    fractionMaxSpeed  = 0.1
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    motionProxy.setStiffnesses("LHipYawPitch", 0.2)
    motionProxy.setStiffnesses("LHipPitch", 0.2)
    motionProxy.setStiffnesses("RHipPitch", 0.2)
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.035065650939941406, 0.18206071853637695, -0.9826618432998657, 
                       0.01609862968325615, -0.38233551383018494, -0.9060218334197998, 
                       -0.1815047711133957, -0.1932658553123474, -0.9233579635620117, 
                       0.3820711076259613, 0.03783803433179855, -0.09672538936138153, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.03785611316561699, -0.17644673585891724, -0.9835819602012634, 
                       0.016386376693844795, 0.37893712520599365, -0.9082373380661011, 
                       0.17751504480838776, 0.19260691106319427, -0.9246478080749512, 
                       -0.3794357478618622, 0.03247988224029541, -0.09699571877717972, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    
    time.sleep(2.0)
    
def userReadyToPlay(motionProxy, postureProxy):
# =============================================================================
# Have to record the transformation for ready to play position
# =============================================================================
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    names  = ["LHipYawPitch", "LHipPitch", "RHipPitch"]
    angles  = [-0.25, -0.7, -0.7]
    fractionMaxSpeed  = 0.1
    motionProxy.setAngles(names, angles, fractionMaxSpeed)

    motionProxy.setStiffnesses("LHipYawPitch", 0.2)
    motionProxy.setStiffnesses("LHipPitch", 0.2)
    motionProxy.setStiffnesses("RHipPitch", 0.2)
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    
    chainName        = "RArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.4127737283706665, -0.21474865078926086, -0.8851559162139893, 
                       0.06692149490118027, -0.907514750957489, -0.17985010147094727, 
                       -0.37956666946411133, -0.29789382219314575, -0.0776839479804039, 
                       0.9599671959877014, -0.26912495493888855, 0.06466364860534668, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
        
    chainName        = "LArm"
    frame            = motion.FRAME_TORSO

    transform       = [0.3653983175754547, 0.20093390345573425, -0.9089057445526123, 
                       0.056045692414045334, 0.911535382270813, -0.2751205563545227, 
                       0.30563390254974365, 0.29891785979270935, -0.18864643573760986, 
                       -0.940177857875824, -0.28368696570396423, 0.04994587600231171, 
                       0.0, 0.0, 0.0, 1.0]
    fractionMaxSpeed = 0.5
    axisMask         = 63 # this value include position and rotation

    motionProxy.setTransforms(chainName, frame, transform, 
                              fractionMaxSpeed, axisMask)
    

    time.sleep(2.0)


def playXylo(motionProxy, keys, dt):
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.1)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.1)
             
            names = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
                     'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand']
            # tempo
            timeList = []
            angleList = []
            for h in range(6):
                t = []
                for i in range(len(keys)): 
                    
                    t.append(dt*(i+1))
                    t.append(dt*(i+1) + 0.07)
                    t.append(dt*(i+1) + 0.1)
                        
                timeList.append(t)   
                
            for j in range(6):
                l = []                
                for k in range(len(keys)):
                            
                    if keys[k] > 5 and keys[k] < 12: 
                        note = list(notes[keys[k]])
                        if j == 4:
                            l.append(note[j])
                            l.append(note[j]+55*almath.TO_RAD)
                            l.append(note[j])
                        else:
                            l.append(note[j])
                            l.append(note[j])
                            l.append(note[j])
# =============================================================================
#                     elif keys[k] == 1:
#                         note = list(notes[10])
#                         if j == 4:
#                             l.append(note[j])
#                             l.append(note[j]+50*almath.TO_RAD)
#                             l.append(note[j])
#                         else:
#                             l.append(note[j])
#                             l.append(note[j])
#                             l.append(note[j])
#                     elif keys[k] == 2:
#                         note = list(notes[6])
#                         if j == 4:
#                             l.append(note[j])
#                             l.append(note[j]+50*almath.TO_RAD)
#                             l.append(note[j])
#                         else:
#                             l.append(note[j])
#                             l.append(note[j])
#                             l.append(note[j])
#                     elif keys[k] == 3:
#                         note = list(notes[8])
#                         if j == 4:
#                             l.append(note[j])
#                             l.append(note[j]+50*almath.TO_RAD)
#                             l.append(note[j])
#                         else:
#                             l.append(note[j])
#                             l.append(note[j])
#                             l.append(note[j])
#                     elif keys[k] == 4:
#                         note = list(notes[9])
#                         if j == 4:
#                             l.append(note[j])
#                             l.append(note[j]+50*almath.TO_RAD)
#                             l.append(note[j])
#                         else:
#                             l.append(note[j])
#                             l.append(note[j])
#                             l.append(note[j])
#                     else:
#                         note = list(notes[8])
#                         if k != len(keys)-1:
#                             nextk = k
#                             for x in range(k+1, len(keys)):
#                                 if keys[x] > 5 and keys[x] < 12:
#                                     nextk = x
#                                     break 
#                             if nextk != k:
#                                 note = list(notes[keys[nextk]])
#                         l.append(note[j])
#                         l.append(note[j])
#                         l.append(note[j])
# =============================================================================
                        
                angleList.append(l)
            
            for h in range(6):
                t = []
                for i in range(len(keys)): 
                    
                    t.append(dt*(i+1))
                    t.append(dt*(i+1) + 0.07)
                    t.append(dt*(i+1) + 0.1)
                        
                timeList.append(t)    
            
            for j in range(6):
                r = []                
                for k in range(len(keys)):
                            
                    if keys[k] > 0 and keys[k] < 6: 
                        note = list(notes[keys[k]])
                        if j == 4:
                            r.append(note[j])
                            r.append(note[j]-55*almath.TO_RAD)
                            r.append(note[j])
                        else:
                            r.append(note[j])
                            r.append(note[j])
                            r.append(note[j])
# =============================================================================
#                     elif keys[k] == 8:
#                         note = list(notes[3])
#                         if j == 4:
#                             r.append(note[j])
#                             r.append(note[j]-50*almath.TO_RAD)
#                             r.append(note[j])
#                         else:
#                             r.append(note[j])
#                             r.append(note[j])
#                             r.append(note[j])
#                     elif keys[k] == 9:
#                         note = list(notes[5])
#                         if j == 4:
#                             r.append(note[j])
#                             r.append(note[j]-50*almath.TO_RAD)
#                             r.append(note[j])
#                         else:
#                             r.append(note[j])
#                             r.append(note[j])
#                             r.append(note[j])
#                     elif keys[k] == 10:
#                         note = list(notes[1])
#                         if j == 4:
#                             r.append(note[j])
#                             r.append(note[j]-40*almath.TO_RAD)
#                             r.append(note[j])
#                         else:
#                             r.append(note[j])
#                             r.append(note[j])
#                             r.append(note[j])
#                     elif keys[k] == 11:
#                         note = list(notes[2])
#                         if j == 4:
#                             r.append(note[j])
#                             r.append(note[j]-45*almath.TO_RAD)
#                             r.append(note[j])
#                         else:
#                             r.append(note[j])
#                             r.append(note[j])
#                             r.append(note[j])
#                     else:
#                         note = list(notes[3])
#                         if k != len(keys)-1:
#                             nextk = k
#                             for x in range(k+1, len(keys)):
#                                 if keys[x] != 0 and keys[x] > 0 and keys[x] < 6:
#                                     nextk = x
#                                     break
#                             if nextk != k:
#                                 note = list(notes[keys[nextk]])
#                         r.append(note[j])
#                         r.append(note[j])
#                         r.append(note[j])
# =============================================================================
                        
                angleList.append(r)
                
            motionProxy.angleInterpolationBezier(names, timeList, angleList)
            
# =============================================================================
# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    postureProxy.goToPosture("Crouch", 0.4)
    userInitPosture(motionProxy, postureProxy)
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
                                   11: robot ask kid try it again\n\
                                   please make selection: "))
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session
            tts.say("Hello, my friend!")
            time.sleep(0.5)
            tts.say("Welcome back to NAO music party!")
            time.sleep(1.0)
            tts.say("Today, we are going to play a lovely song!")
            ledProxy.randomEyes(2.0)
            tts.say("Let me show you what I have learned lately!")
            time.sleep(0.5)   
# =============================================================================
#           Play twinkle twinkle
            dt = 0.6
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]

            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            tts.say("Do you recognize this song from somewhere?")
            time.sleep(3.0)
            tts.say("Yes, it is the the most popular Twinkle Twinkle Little Star!")
            time.sleep(1.0)
#           may use speech recognition instead of this
            tts.say("Do you like it?")
            time.sleep(3.0)
            tts.say("Do you want to hear another one?")
            if int(raw_input("1 for play new song, 2 for no:")):
                
                tts.say("Great! Let me tell you how to play this song")
            
# =============================================================================
# =============================================================================
#       task 1: Start single note play without color
        elif taskNumber == 1:
            
            keys = [6]
            name = 'FaceLeds'
            colorName1 = 'blue'
            duration = 1.0
        
            ledProxy.fadeRGB(name, colorName1, duration)
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("I just played a note, can you repeat that note for me?")
            time.sleep(1.0)
            tts.say("You may find a pair of red head mallet \
                    on the table somewhere.")
            time.sleep(1.0)
            tts.say("I want you to pick them up, \
                    and use one of them to play that note.")

        
# =============================================================================
#       task 2: Start single note play along with color  
        elif taskNumber == 2: 
            
            keys = [8]
            name = 'FaceLeds'
            colorName2 = 'green'
            duration = 1.0
            
            tts.say("Wonderful! Here comes an other one!")
            ledProxy.fadeRGB(name, colorName2, duration)
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)    
            tts.say("This is a new note, can you repeat that note for me?")
            time.sleep(5.0)
            tts.say("Have you notice that my eye color matchs the note color?")
            time.sleep(2.0)
            tts.say("Let's try it again, I am going to hit the green bar now, \
                    listen carefully!")
            ledProxy.fadeRGB(name, colorName2, duration)
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Now, it is your turn to play the green bar!")
            tts.say("And try to use your left hand to do this.")

        
# =============================================================================
#       task 3: Start multiple notes play along with color
        elif taskNumber == 3:
                
            keys = [1,5,6]
            dt1 = 1
            name = 'FaceLeds'
#            colorNames = ['red', 'green', 'blue']
            duration = 0.5
            
            tts.say("In the next part we are going to have more fun!")
            ledProxy.randomEyes(2.0)
        
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            
            playXylo(motionProxy, keys, dt1)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("I just played three notes, can you repeat them for me?")
            time.sleep(5.0)
            tts.say("Great Job!")
            time.sleep(1.0)
            tts.say("Now, if you can sing the color while hitting the note \
                    that would be even better!")
            time.sleep(5.0)
            tts.say("Well done!")
            tts.say("Do you want to try it again?")
        
# =============================================================================
#       task 4: Start play whole song 
#       first half song
        elif taskNumber == 4:
            
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5
            
            tts.say("Here comes the ultimate challenge!")
            tts.say("We are going to play the Twinkle Twinkle Song \
                    for the rest of the session.")
            time.sleep(1.0)
            tts.say("Here comes the first half of the song! \
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt1)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")

# =============================================================================
#       task 5: Start play whole song 
#       second half song 
        elif taskNumber == 5:
            
            keys = [5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the second half of the song! \
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt1)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")

# =============================================================================
#       task 6: play the whole song
        elif taskNumber == 6:
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the whole song! \
                    Listen and watch carefully.")
            tts.say("I will use normal speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)

            playXylo(motionProxy, keys, dt)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(1.0)
            tts.say("Now, it is your turn to play.")      

# =============================================================================
#       task 7: take a break for 180 seconds      
        elif taskNumber == 7:
            
            tts.say("Do you want to take a break?")
            tts.say("You will have 180 seconds \
                    for a short break!")
            tts.say("Starting now!")
            ledProxy.randomEyes(3.0)
            time.sleep(57)
            tts.say("You have 120 seconds left.")
            ledProxy.randomEyes(3.0)
            time.sleep(57)
            tts.say("You have one minunt left.")
            ledProxy.randomEyes(3.0)
            time.sleep(57)
            tts.say("Shall we start the next task?")  
        
# =============================================================================
#       task 8: free play
        elif taskNumber == 8:
            
            tts.say("We are done with practice today.")
            time.sleep(1.0)
            tts.say("Feel free to stay and play whatever song you may like.")
            time.sleep(1.0)

# =============================================================================
#       task 9: end the session get out the loop
        elif taskNumber == 9:
            tts.say("Have a nice day! See you next time!")            
            motionProxy.rest()
            break
        
#       other typo or mistakes
            
        elif taskNumber == 10:
            tts.say("Do you want me to show you again?")
            motionProxy.rest()
            
        elif taskNumber == 11:
            tts.say("It looks like you may need want to try it again.")
            
        elif taskNumber == 
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