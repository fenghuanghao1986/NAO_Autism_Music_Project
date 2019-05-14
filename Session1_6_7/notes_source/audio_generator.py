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
import numpy as np
import shh
import os
import datetime
import recordplay
import argparse
import copy
#import motion
import stft
from naoqi import ALProxy
import time

host = "192.168.0.2"
username = "nao"
pw = "nao"
modeList = ['easy', 'hard']
gameList = ['feeling', 'distinguish', 'play', 'match']

def createMisc(uncfList, comfList, n, game, count):
    
    play = []
        
    u_cList = raw_input("select comfortable list type u or c: ")

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
    print(play)
    newFile = game + count + u_cList +  '.wav'
    wav.write(newFile, rate, newData)
        
    dst = '/home/nao/' + newFile
    # this path need to be changed
    origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
    sshFile = shh.SSHConnection(host, username, pw)
    sshFile.put(origin, dst)
    sshFile.close()
    
    return (dst, play)

def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)

    uncfList = ['0','3','4','7','8','10','11']
    comfList = ['0','1','2','4','5','6','8','9']
#    uncfList = ['1', '2']
#    comfList = ['3', '4']
#    now = datetime.datetime.now()
    # =============================================================================
    # 
    # =============================================================================
#    mode = raw_input("select mode level type e or h: ")
#    tts.say("Let's play a game!")
#    time.sleep(1.0)
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
        n = 16

        # find a way to combine single note files
        # send to robot and play on it
        tts.say("Welcome to the Feel the difference game!")
        time.sleep(1.0)
        tts.say("In this game you will hear two pieces of music.")
        time.sleep(0.5)
        tts.say("After I played, you may tell me what do you feel about them.")
        time.sleep(0.5)
        tts.say("You can say Same or Different to tell me the answer!")
        time.sleep(0.5)
        tts.say("Let's begin!")
        (dst1, play1) = createMisc(uncfList, comfList, n, game, count)
        tts.say("This is the first piece of music, feel it carefully!")
        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT, dst1)
        (dst2, play2) = createMisc(uncfList, comfList, n, game, count)
        tts.say("This is the second pieces of music, feel it carefully!")
        recordplay.playBack(robotIP, PORT, dst2)
        time.sleep(15)
        tts.say("Now, you may tell me what do you feel about those two music piece?")
        tts.say("Are they feel same or different?")
        time.sleep(5)
        tts.say("Good! I understand how you feel about music now!")
        time.sleep(2)
        
    #    tts to say and provide feedback
    # =============================================================================
    #     nao plays two pieces of audios and kid tell if they are same or not
    # =============================================================================
        return
#    elif game == 'd':
#        
#        n = 6
#        tts.say("Welcome to the Play What your Heard game!")
#        time.sleep(1.0)
#        tts.say("In this game you will hear one short piece of music.")
#        time.sleep(0.5)
#        tts.say("After I played, you may try to play it on xylophone.")
#        time.sleep(0.5)
#        tts.say("Try your best to match them, there is no right or wrong!")
#        time.sleep(0.5)
#        tts.say("Just have fun!")
#        tts.say("Let's begin!")
#        play = []
#        if u_cList == 'u':
#            for i in range(n):
#                play.append(random.choice(uncfList))
#        else:
#            for i in range(n):
#                play.append(random.choice(comfList))
#        newData = []
#        for j in play:
#            rate, data = wav.read(str(j) + '.wav')
#            if len(newData) == 0:
#                newData = copy.deepcopy(data)
#            else:
#                newData = np.concatenate((newData, data), axis=0)
#        newFile = game + count + '.wav'
#        wav.write(newFile, rate, newData)
#        
#        dst = '/home/nao/' + newFile
#        # this path need to be changed
#        origin = os.path.join(r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source', newFile)
#        sshFile = shh.SSHConnection(host, username, pw)
#        sshFile.put(origin, dst)
#        sshFile.close()
        
#        recordplay.record(robotIP, PORT, t=5)
#        recordplay.playBack(robotIP, PORT, dst)
    #    tts to say and provide feedback
    # =============================================================================
    #     after nao play the audio, kid should try to re-play that
    # =============================================================================
#        return
    elif game == 'p':
        n = 3
        tts.say("Welcome to the Play What your Heard game!")
        time.sleep(1.0)
        tts.say("In this game you will hear one short piece of music.")
        time.sleep(0.5)
        tts.say("After I played, you may try to play it on xylophone.")
        time.sleep(0.5)
        tts.say("Try your best to match them, there is no right or wrong!")
        time.sleep(0.5)
        tts.say("Just have fun!")
        tts.say("Let's begin!")     
        (dst, play) = createMisc(uncfList, comfList, n, game, count)
        tts.say("This is the piece of music, feel it carefully!")
        recordplay.playBack(robotIP, PORT, dst)
        time.sleep(4)
        tts.say("Now, it is your time to play!")    
        recordplay.record(robotIP, PORT, t=8)
#        recordplay.playBack(robotIP, PORT)
        origin = '/home/nao/test.wav'
        local = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\notes_source\test.wav'
        sshFile = shh.SSHConnection (host, username, pw)
        sshFile.get(origin, local)
        sshFile.close()
       
        sampleRate, data = wav.read(local)
#        N = len(data)
        Nwin = 2048
        xx = data[:, 0]
            
        low = 1040
        high = 2800
        x = stft.bandpass_filter(xx, low, high, sampleRate, order=3)
            # Generate a chirp: start frequency at 5 Hz and going down at 2 Hz/s
#        totleTime = np.arange(N) / sampleRate  # seconds
        #    x = np.cos(2 * np.pi * time * (5 - 2 * 0.5 * time))
        
            # Test with Nfft bigger than Nwin
#        Nfft = Nwin * 2
        s = np.abs(stft.stft(x, Nwin))
#        y = stft.istft(s, Nwin)
        peaks = stft.findNotes(s, sampleRate/2)
        realPeaks = stft.realPeak(peaks)
        print(realPeaks)
        start = time.time()
#        r_len = len(realPeaks)
#            change orgpeaks to the key that nao just played or the music just played
#           find a way please!
        o_len = len(play)
#            result = [[-1 for i in range(len(realPeaks))] for j in range(len(orgPeaks))]
        
        diff = stft.LevDist2(realPeaks, play)
        sim = 1 - (float(diff)/(float(o_len)))
        end = time.time()
        print("stft time: " + str(end - start))
        print(diff, sim)
        if sim >= 0.7:
            tts.say("Wonderful! You are a music master!!")
        elif sim > 0.4 and sim < 0.7:
            tts.say("Great job! I cannot believe you made it!")
        else:
            tts.say("Nice! I am sure you did your best!")
        
    #    tts to say and provide feedback
    # =============================================================================
    #     find proper color, after nao play the audio, kid should say the color names
    # =============================================================================
        return
    else:
        
        dst = createMisc(uncfList, comfList, n, game, count)

#        recordplay.record(robotIP, PORT, t=5)
        recordplay.playBack(robotIP, PORT, dst)
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