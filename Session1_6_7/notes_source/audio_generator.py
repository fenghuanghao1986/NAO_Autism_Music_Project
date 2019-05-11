# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:06:47 2019

@author: fengh
"""

# This is the create music game test function
# contains easy and hard modes
# game type:
# 1. music feeling: describe the feeling between different combo of notes
# 2. ear play 1: listen two piece of notes with slicely difference or same 
# 3. ear play 2: listen one piece and play it on xylophone robot provide feedback

import random
from scipy.io import wavfile as wav
#import numpy as np
import shh
import os
import datetime
import recordplay
import argparse
import copy


host = "192.168.0.2"
username = "nao"
pw = "nao"
modeList = ['easy', 'hard']
gameList = ['feeling', 'distinguish', 'play', 'match']

def game(robotIP, PORT=9559):
#    uncfList = ['3','4','7','8','10','11']
#    comfList = ['1','2','4','5','6','8','9']
    uncfList = ['1', '2']
    comfList = ['3', '4']
    n = 3
    play = []
    now = datetime.datetime.now()
    # =============================================================================
    # 
    # =============================================================================
#    mode = raw_input("select mode level type e or h: ")
    u_cList = raw_input("select comfortable list type u or c: ")
    game = raw_input("select game name type f d p or m: ")
    count = raw_input("type how many times kid play game: ")
    # =============================================================================
    # 
    # =============================================================================


    # =============================================================================
    # nao play one piece or two, kid should tell if they feel same or not and what 
    # do they fell
    # =============================================================================
    if game == 'f':
        # find a way to combine single note files
        # send to robot and play on it
        if u_cList == 'u':
            for i in range(n):
                play.append(random.choice(uncfList))
        else:
            for i in range(n):
                play.append(random.choice(comfList))
        newData = []
        for j in play:
            rate, data = wav.read(str(j) + '.wav')
            if len(newData) == 0:
                newData = copy.deepcopy(data)
            else:
                newData = np.concatenate((newData, data), axis=0)
        newFile = game + count + '.wav'
        wav.write(newFile, rate, newData)
        
        dst = '/home/nao/' + newFile
        # this path need to be changed
        origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
        sshFile = SSHConnection(host, username, pw)
        sshFile.put(origin, dst)
        sshFile.close()
        
#        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT, dst)
    #    tts to say and provide feedback
    # =============================================================================
    #     nao plays two pieces of audios and kid tell if they are same or not
    # =============================================================================
        return
    elif game == 'd':
        if u_cList == 'u':
            for i in range(n):
                play.append(random.choice(uncfList))
        else:
            for i in range(n):
                play.append(random.choice(comfList))
        newData = []
        for j in play:
            rate, data = wav.read(str(j) + '.wav')
            newData = np.vstack((data, newData))
        newFile = game + now + count + '.wav'
        wav.write(newFile, rate, newData)
        
        dst = '/home/nao/' + newFile
        # this path need to be changed
        origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
        sshFile = ssh("SSHConnection", host, username, pw)
        sshFile.get(origin, dst)
        sshFile.close()
        
        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT)
    #    tts to say and provide feedback
    # =============================================================================
    #     after nao play the audio, kid should try to re-play that
    # =============================================================================
        return
    elif game == 'p':
        if u_cList == 'u':
            for i in range(n):
                play.append(random.choice(uncfList))
        else:
            for i in range(n):
                play.append(random.choice(comfList))        
        newData = []
        for j in play:
            rate, data = wav.read(str(j) + '.wav')
            newData = np.vstack((data, newData))
        newFile = game + now + count + '.wav'
        wav.write(newFile, rate, newData)
        
        dst = '/home/nao/' + newFile
        # this path need to be changed
        origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
        sshFile = ssh("SSHConnection", host, username, pw)
        sshFile.get(origin, dst)
        sshFile.close()
        
        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT)
    #    tts to say and provide feedback
    # =============================================================================
    #     find proper color, after nao play the audio, kid should say the color names
    # =============================================================================
        return
    else:
        if u_cList == 'u':
            for i in range(n):
                play.append(random.choice(uncfList))
        else:
            for i in range(n):
                play.append(random.choice(comfList))        
        newData = []
        for j in play:
            rate, data = wav.read(str(j) + '.wav')
            newData = np.vstack((data, newData))
        newFile = game + now + count + '.wav'
        wav.write(newFile, rate, newData)
        
        dst = '/home/nao/' + newFile
        # this path need to be changed
        origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
        sshFile = ssh("SSHConnection", host, username, pw)
        sshFile.get(origin, dst)
        sshFile.close()
        
        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT)
    #    tts to say and provide feedback
        return
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.0.2",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port) 