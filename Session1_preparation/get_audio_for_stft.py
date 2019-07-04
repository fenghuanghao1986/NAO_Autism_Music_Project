# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:55:41 2019

@author: CV_LAB_Howard
"""

import recordplay
import ssh
import time

host = "192.168.0.3"
username = "nao"
pw = "nao"
print("ready to record in 3 seconds")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("start recording")
recordplay.record(host, 9559, t=30)
print("stop record!")
    
origin = '/home/nao/uplay.wav'
dst = r'C:\Users\fengh\Desktop\test_sampe_for_stft.wav'

sshFile = ssh.SSHConnection(host, username, pw)
print("start downloading...")
sshFile.get(origin, dst)
print("download complete!")
sshFile.close()