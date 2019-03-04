# -*- coding: utf-8 -*-
"""
Left and Right arm
"""
import time
import motion
import almath
import positions
from naoqi import ALProxy
posture = "chill"

class Effector:
    def __init__(self, IP, PORT):
        global posture

        try:
            self.motionProxy = ALProxy("ALMotion", IP, PORT)
        except Exception, e:
            print "could not create motion proxy"
            print "problem was: ", e
        self.motionProxy.setStiffnesses("Body", 1)
        self.get_ready()
        time.sleep(1)
        self.chill()
        posture = "chill" 
        self.motionProxy.setStiffnesses("Body", 1)


    def hit_key(self,key, sleep_time=0.5):
        """
        Hit the specified key
        :param key: char corresponding to key (Upper case) (e.g. 'C')
        :param sleep_time:
        """
        arm,position,default = positions.get_position(key)
        self.move_to_absolute_position(position,default,arm)
        time.sleep(sleep_time)
        
    def get_ready(self):
        """
        Get in hitting position
        """
        global posture

        if posture == "getready":
            return
        
        self.motionProxy.setStiffnesses("Body", 1)
        time.sleep(1)
        self.motionProxy.setAngles('Body', [-0.05526590347290039, 0.1318819522857666, 0.7224719524383545, 0.059783935546875, -1.1980957984924316, -0.30368995666503906, -1.8238691091537476, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.533958077430725, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5340418815612793, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.7194879055023193, 0.007627964019775391, 1.4158400297164917, 0.14730596542358398, 1.8238691091537476, 0.9451999664306641],0.1)
        time.sleep(2)     
        
        self.motionProxy.setAngles('Body', [-0.05526590347290039, 0.1318819522857666, 0.4463520050048828, 0.4862360954284668, -1.1612801551818848, -0.2990880012512207, -1.8238691091537476, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.535889744758606, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5355758666992188, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.42649388313293457, -0.3298518657684326, 1.2777800559997559, 0.10281991958618164, 1.8238691091537476, 0.9451999664306641],0.1)
        time.sleep(3)        
        self.motionProxy.setAngles('Body', [-0.05373191833496094, 0.16563010215759277, 0.4340801239013672, 0.837522029876709, 0.4279439449310303, -0.3481760025024414, -0.8882279396057129, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.5354920625686646, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5355758666992188, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.561486005783081, -0.6029040813446045, -0.06753802299499512, 0.1043539047241211, 0.7592880725860596, 0.9459999799728394],0.1)
        
        posture = "getready"

    def closeHands(self):
        self.motionProxy.closeHand('LHand')
        self.motionProxy.stiffnessInterpolation('LHand', 1, 0.01)
        self.motionProxy.closeHand('RHand')
        self.motionProxy.stiffnessInterpolation('RHand', 1, 0.01)
        
    def openHands(self):
        self.motionProxy.stiffnessInterpolation('LHand', 0, 0.01)
        self.motionProxy.stiffnessInterpolation('RHand', 0, 0.01)      
        
    def chill(self):
        """
        Get in resting position
        """
        global posture        
        
        if posture == "chill":
            return
        
        time.sleep(1)        
        self.motionProxy.setAngles('Body', [-0.05373191833496094, 0.16563010215759277, 0.4340801239013672, 0.837522029876709, 0.4279439449310303, -0.3481760025024414, -0.8882279396057129, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.5354920625686646, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5355758666992188, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.561486005783081, -0.6029040813446045, -0.06753802299499512, 0.1043539047241211, 0.7592880725860596, 0.9459999799728394],0.1)
        time.sleep(2)             
        self.motionProxy.setAngles('Body', [-0.05526590347290039, 0.1318819522857666, 0.4463520050048828, 0.4862360954284668, -1.1612801551818848, -0.2990880012512207, -1.8238691091537476, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.535889744758606, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5355758666992188, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.42649388313293457, -0.3298518657684326, 1.2777800559997559, 0.10281991958618164, 1.8238691091537476, 0.9451999664306641],0.1)
        time.sleep(2)
        self.motionProxy.setAngles('Body', [-0.05526590347290039, 0.1318819522857666, 0.7224719524383545, 0.059783935546875, -1.1980957984924316, -0.30368995666503906, -1.8238691091537476, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.533958077430725, 1.2885180711746216, 0.9188239574432373, 4.1961669921875e-05, -0.8298521041870117, -0.3803901672363281, -1.5340418815612793, 1.3775739669799805, 0.8606162071228027, 0.04146003723144531, 0.7194879055023193, 0.007627964019775391, 1.4158400297164917, 0.14730596542358398, 1.8238691091537476, 0.9451999664306641],0.1)
        time.sleep(4)        
        self.motionProxy.setStiffnesses("Body", 0)
        
        posture = "chill"

    def move_to_absolute_position(self, position, default, arm):
        if arm == 'LArm':
            wrist = 'LWristYaw'
        else: 
            wrist = 'RWristYaw'
        #print(arm)
        #print(position)
        self.motionProxy.setAngles(arm,position[0],1)
        time.sleep(0.25)
        self.motionProxy.setAngles(wrist,position[1],1)
        time.sleep(0.4)
        self.motionProxy.setAngles(arm,position[0],1)
        time.sleep(0.15)
        self.motionProxy.setAngles(arm,default,1)            
    
    def get_absolute_position(self,arm):
        keys = self.motionProxy.getAngles(arm, True)
        return keys          
        
    def set_stiff(self, true, hand):
        """
        Set the hand stiffness
        :param true: true if stiff, false if not
        :param hand: left or right 'LHand'/'RHand'
        """
        self.motionProxy.stiffnessInterpolation(hand, int(true), 0.01)