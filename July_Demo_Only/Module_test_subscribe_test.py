# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:36:09 2019

@author: CV_LAB_Howard
"""

from naoqi import ALProxy, ALBroker, ALModule
import time
check = 0


# create python module
class myModule(ALModule):
  """python class myModule test auto documentation : comment needed to create a new python module"""


  def pythondatachanged(self, strVarName, value):
    """callback when data change"""
    print "datachanged", strVarName, " ", value, " ", strMessage
    global check
    check = 1

  def _pythonPrivateMethod(self, param1, param2, param3):
    global check


broker = ALBroker("pythonBroker","10.0.252.184",9999,"naoverdose.local",9559)


# call method
try:

  pythonModule = myModule("pythonModule")
  prox = ALProxy("ALMemory")
  #prox.insertData("val",1) # forbiden, data is optimized and doesn't manage callback
  prox.subscribeToEvent("WordRecognized","pythonModule", "pythondatachanged") #  event is case sensitive !

except Exception,e:
  print "error"
  print e
  exit(1)

while (1):
  time.sleep(2)