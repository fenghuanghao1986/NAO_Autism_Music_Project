# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:23:50 2019

@author: CV_LAB_Howard
"""

# test 
import numpy as np
import almath

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

# input vars
# input keys
keys = [3,0,6,0,0,8,7,0,6,0,0,10,0,9,0,0,7,0,0,6,0,8,7,0,5,0,0,7,0,3,0,1,3]
# names always the same
names = ['RArm', 'LArm']
# tempo
dt = 1
n = len(keys)

leftTimeList = []

for h in range(6):
    t = []
    for i in range(len(keys)): 
        
        if keys[i] == 0:
            t.append(dt*i)
            t.append(dt*i)
            t.append(dt*i)
        else:
            t.append(dt*i)
            t.append(dt*i + 0.07)
            t.append(dt*i + 0.1)
            
    leftTimeList.append(t)   

leftAngleList = []

for j in range(6):
    
    angleList = []
    
    for k in keys:
                
        if k > 5 and k < 12: 
            note = list(notes[k])
        else:
            note = list(notes[8])
        if k == 4:
            angleList.append(note[j])
            angleList.append(note[j]+35*almath.TO_RAD)
            angleList.append(note[j])
        else:
            angleList.append(note[j])
            angleList.append(note[j])
            angleList.append(note[j])
            
    leftAngleList.append(angleList)

rightTimeList = []
for h in range(6):
    t = []
    for i in range(len(keys)): 
        
        if keys[i] == 0:
            t.append(dt*i)
            t.append(dt*i)
            t.append(dt*i)
        else:
            t.append(dt*i)
            t.append(dt*i + 0.07)
            t.append(dt*i + 0.1)
            
    rightTimeList.append(t)   

rightAngleList = []

for j in range(6):
    
    angleList = []
    
    for k in keys:
                
        if k > 0 and k < 6: 
            note = list(notes[k])
        else:
            note = list(notes[3])
        if k == 4:
            angleList.append(note[j])
            angleList.append(note[j]+45*almath.TO_RAD)
            angleList.append(note[j])
        else:
            angleList.append(note[j])
            angleList.append(note[j])
            angleList.append(note[j])
            
    rightAngleList.append(angleList)
    
angleList = [rightAngleList, leftAngleList]
timeList = [rightTimeList, leftTimeList]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    