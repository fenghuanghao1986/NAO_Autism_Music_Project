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
# Right Arm
notes[1] = [1.2180380821228027, -0.9189081192016602, 1.514016032218933, 
             0.6151759624481201, -0.7210218906402588, 0.22960001230239868]

notes[2] = [1.2257080078125, -0.8038580417633057, 1.5094140768051147, 
             0.6427879333496094, -0.6719338893890381, 0.22960001230239868]

notes[3] = [1.211902141571045, -0.7302260398864746, 1.515550136566162, 
             0.7056820392608643, -0.6980118751525879, 0.22960001230239868]

notes[4] = [1.2011637687683105, -0.6151759624481201, 1.5078800916671753, 
             0.7563040256500244, -0.7609059810638428, 0.22960001230239868]

#notes[5] = [1.1029877662658691, -0.49859189987182617, 1.501744031906128, 
#           0.84527587890625, -0.9971418380737305, 0.23000001907348633]
notes[5] = [1.182755947113037, -0.48325204849243164, 1.5109480619430542, 
             0.7977218627929688, -0.8698201179504395, 0.22960001230239868]
# Left Arm
notes[6] = [0.9480281066894531, 0.3328361511230469, -1.512566089630127, 
             -0.7669579982757568, 1.2271580696105957, 0.2239999771118164]

notes[7] = [1.0691561698913574, 0.5491299629211426, -1.4205260276794434, 
             -0.8053081035614014, 0.9617760181427002, 0.23040002584457397]

notes[8] = [1.0568840503692627, 0.6581020545959473, -1.4220600128173828, 
             -0.8252501487731934, 0.9893879890441895, 0.23240000009536743]

notes[9] = [1.1075060367584229, 0.7684919834136963, -1.4650120735168457, 
             -0.7915019989013672, 0.8482601642608643, 0.29600000381469727]

notes[10] = [1.3207321166992188, 0.8283181190490723, -1.679771900177002, 
             -0.8620660305023193, 0.8682019710540771, 0.22640001773834229]

notes[11] = [1.3529460430145264, 0.931096076965332, -1.679771900177002, 
             -0.7500841617584229, 0.7638900279998779, 0.225600004196167]

# =============================================================================
# The following function initializes NAO's starting position or resting position
# =============================================================================
def userInitPosture(motionProxy, postureProxy):
# =============================================================================
#     # this function should have NAO crouching position with leg joints rest/locked?
#     # and both arms should be straight down without touching legs and other parts
# =============================================================================
    
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
    
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    time.sleep(5.0)
    
def userReadyToPlay(motionProxy, postureProxy):
# =============================================================================
# Have to record the transformation for ready to play position
# =============================================================================

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
    

    time.sleep(2.0)
    
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
    
    
    motionProxy.setStiffnesses("LLeg", 0.2)
    motionProxy.setStiffnesses("RLeg", 0.2)
    


    time.sleep(5.0)
    
def playXylophone(motionProxy, keys, dt):
    # input notes is dictionary type, including key as note, and 
    # values as set of angles
    # anglse related to hit will be a seperate list
   
    motionProxy.setStiffnesses("LArm", 1)
    motionProxy.setStiffnesses("RArm", 1)
    
    for key in keys:        
        # identify which hand to use to find and hit current note
        if key == 0:
            time.sleep(0.3)
        elif key > 0 and key < 6:
            
#            names = ['RArm', 'RWristYaw']
#            names = ['LArm']
            useSensors  = True
            
#            current_note = motionProxy.getAngles('RArm', useSensors)
            target_note = list(notes[key])
            
            # since for 'R/LArm' has 6 angles invoved, so we have to assign
            # 6 interpolations for each of the joint
            angleList = [[target_note[0]], 
                          [target_note[1]],
                          [target_note[2]],
                          [target_note[3]],
                          [target_note[4]],
                          [target_note[5]]]
#                          [beforeHit[0], onHit, afterHit[0]]]
            
            timeList = [[dt],
                        [dt],
                        [dt],
                        [dt],
                        [dt],
                        [dt]]
            
            motionProxy.angleInterpolationBezier(['RArm'], timeList, angleList)
            
            beforeHit = motionProxy.getAngles('RWristYaw', useSensors)
            onHit = beforeHit[0] - 45*almath.TO_RAD
            afterHit = beforeHit[0] 
            motionProxy.setAngles("RHand", 0.22, 1)

            angleLists = [[onHit, afterHit]]
            timeLists  = [[0.07, 0.1]]
        
            motionProxy.angleInterpolationBezier(['RWristYaw'], 
                                                 timeLists, angleLists)
            
        else:
            
#            names = ['LArm', 'LWristYaw']
#            names = ['LArm']
            useSensors  = True
            
#            current_note = motionProxy.getAngles('LArm', useSensors)
            target_note = list(notes[key])
            
            # since for 'R/LArm' has 6 angles invoved, so we have to assign
            # 6 interpolations for each of the joint
            angleList = [[target_note[0]], 
                          [target_note[1]],
                          [target_note[2]],
                          [target_note[3]],
                          [target_note[4]],
                          [target_note[5]]]
#                          [beforeHit[0], onHit, afterHit[0]]]
            
            timeList = [[dt],
                        [dt],
                        [dt],
                        [dt],
                        [dt],
                        [dt]]
            
            motionProxy.angleInterpolationBezier(['LArm'], timeList, angleList)
            
            beforeHit = motionProxy.getAngles('LWristYaw', useSensors)
            onHit = beforeHit[0] + 35*almath.TO_RAD
            afterHit = beforeHit[0] 
            motionProxy.setAngles("LHand", 0.22, 1)

            angleLists = [[onHit, afterHit]]
            timeLists  = [[0.07, 0.1]]
        
            motionProxy.angleInterpolationBezier(['LWristYaw'], 
                                                 timeLists, angleLists)
            
# =============================================================================
# 
# =============================================================================
def main(robotIP, PORT=9559):
    
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)  
    ledProxy = ALProxy("ALLeds", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    
# =============================================================================      
# =============================================================================
#   creating for loop to control the task including repeat task and take break
    for i in range(1000):
        
        taskNumber = int(raw_input("select task:\n\
                                   1: single note play\n\
                                   2: single note with color\n\
                                   3: multiple notes with color\n\
                                   4: first half song practice\n\
                                   5: second half song practice\n\
                                   6: whole song play\n\
                                   7: take break\n\
                                   8: free play\n\
                                   9: end session\n\
                                   0: intro\n\
                                   please make selection: "))
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session
            tts.say("Hello, my friend!")
            time.sleep(0.5)
            tts.say("Welcome to NAO music party!")
            time.sleep(1.0)
            tts.say("Today, we are going to play a migical song!")
            ledProxy.randomEyes(3.0)
            tts.say("Let me show you what I have learned lately!")
            time.sleep(0.5)   
# =============================================================================
#           Start play Harry Potter Theme as demo
#           NAO plays Harry Potter Theme
            keys = [3,0,6,0,0,8,7,0,6,0,0,10,0,9,0,0,7,0,0,6,0,8,7,0,5,0,0,7,0,3,0,1,3,
                    3,0,6,0,0,8,7,0,6,0,0,10,0,9,0,0,7,0,0,6,0,8,7,0,5,0,0,7,0,3,0,1,3]

            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.3)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy, postureProxy)
            ledProxy.randomEyes(2.0)
            tts.say("Do you recognize this song from somewhere?")
            time.sleep(3.0)
            tts.say("Yes, it is the the most popular theme from Movie Harry Potter!")
            time.sleep(1.0)
#           may use speech recognition instead of this
            tts.say("Do you like it?")
            time.sleep(3.0)
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
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.3)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("I just played a note, can you repeat that note for me?")
            time.sleep(1.0)
            tts.say("You may find a pair of red head mallet \
                    on the table somewhere.")
            time.sleep(1.0)
            tts.say("I want you to pick them up, \
                    and use one of them to play that note.")
            time.sleep(5.0)
            # may have to create a if condition depending on user's response
            tts.say("Do you want to try this again?")
        
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
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.3)
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
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.3)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Now, it is your turn to play the green bar!")
            tts.say("And try to use your left hand to do this.")
            time.sleep(5.0)
            tts.say("Do you want to try this again?")
        
# =============================================================================
#       task 3: Start multiple notes play along with color
        elif taskNumber == 3:
                
            keys = [3, 6, 8]
            name = 'FaceLeds'
#            colorNames = ['red', 'green', 'blue']
            duration = 0.5
            
            tts.say("In the next part we are going to have more fun!")
            ledProxy.randomEyes(2.0)
        
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.5)
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
            
            keys = [3,6,8,7,6,10,9,7]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5
            
            tts.say("Here comes the ultimate challenge!")
            tts.say("We are going to play the Harry Potter Song \
                    for the rest of the session.")
            time.sleep(1.0)
            tts.say("Here comes the first half of the song! \
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 1)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(2.0)
            tts.say("Now, it is your turn to play.")
            time.sleep(20.0)
            tts.say("Do you want to try it again?")
        
# =============================================================================
#       task 5: Start play whole song 
#       second half song 
        elif taskNumber == 5:
            
            keys = [6,8,7,5,7,3,1,3]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the second half of the song! \
                    Listen and watch carefully.")
            tts.say("I will use slower speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 1)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(2.0)
            tts.say("Now, it is your turn to play.")
            time.sleep(20.0)
            tts.say("Do you want to try it again?")

# =============================================================================
#       task 6: play the whole song
        elif taskNumber == 6:
            keys = [3,0,6,0,0,8,7,0,6,0,0,10,0,9,0,0,7,0,0,
                    6,0,8,7,0,5,0,0,7,0,3,0,1,0,3]
            name = 'FacdLeds'
#            colorRGB = ['0x00FF0000', '0x0000FF00', '0x000000FF',
#                        '0x00FF00FF', '0x00C0C0C0', '0x00A16400']
            duration = 0.5

            tts.say("Here comes the whole song! \
                    Listen and watch carefully.")
            tts.say("I will use normal speed to play.")
            userInitPosture(motionProxy, postureProxy)
            userReadyToPlay(motionProxy, postureProxy)
            motionProxy.setAngles("RArm", 
                                  [1.211902141571045, -0.7302260398864746, 
                                   1.515550136566162, 0.7056820392608643, 
                                   -0.6980118751525879, 0.22960001230239868], 
                                   0.3)
            time.sleep(2.0)
            motionProxy.setAngles("LArm", 
                                  [1.0568840503692627, 0.6581020545959473, 
                                   -1.4220600128173828, -0.8252501487731934, 
                                   0.9893879890441895, 0.23240000009536743], 
                                   0.3)
            time.sleep(2.0)
            playXylophone(motionProxy, keys, dt = 0.3)
            userReadyToPlay(motionProxy, postureProxy)
            userInitPosture(motionProxy,postureProxy)
            tts.say("Did you get it?")
            time.sleep(2.0)
            tts.say("Now, it is your turn to play.")
            time.sleep(20.0)
            tts.say("Do you want to try it again?")            

# =============================================================================
#       task 7: take a break for 180 seconds      
        elif taskNumber == 7:
            
            tts.say("Do you want to take a break?")
            tts.say("You will have one hundred and eighty seconds \
                    for a short break!")
            tts.say("Starting now!")
            ledProxy.randomEyes(5.0)
            time.sleep(180)
            tts.say("Shall we start the next task?")  
        
# =============================================================================
#       task 8: free play
        elif taskNumber == 8:
            
            tts.say("We are done learning Harry Potter song today.")
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
        else:
            continue
        
# =============================================================================
# Calling the main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
#    parser.add_argument("--ip", type=str, default="192.168.0.2",
#                        help="Robot ip address")
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)    
# =============================================================================
# End of the test session program