# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:55:41 2019

@author: CV_LAB_Howard
"""

import recordplay
import ssh

host = "192.168.0.2"
username = "nao"
pw = "nao"

recordplay.record(host, 9559, t=30)
    
origin = '/home/nao/uplay.wav'
dst = r'C:\Users\fengh\Desktop\test_sampe_for_stft.wav'
 
ssh = SSHConnection(host, username, pw)
ssh.get(origin, dst)
ssh.close()