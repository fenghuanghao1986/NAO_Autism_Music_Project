# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:36:12 2019

@author: fengh
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:53:15 2019

@author: CV_LAB_Howard
"""
# =============================================================================
# This is a find notes and hit template 
# =============================================================================
#import almath
import time
import sys
import csv
import datetime

print "Enter subject number:\n"
subject = raw_input()
print "Enter session number:\n"
session = raw_input()
now = datetime.datetime.now()
day = str(now.day)
mon = str(now.month)
year = str(now.year)
task = 0
keys = []
fileName = subject + '_' + session  + '_' + year + '_' + mon + '_' + day + '.csv'

try:
    with open(fileName, 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['task', 'ground_truth', 'kid_input', 'result'])

        filewriter.writerow(['01', '123', '122', '.667'])
        filewriter.writerow(['01', '123', '122', '.667'])
        filewriter.writerow(['01', '123', '122', '.667'])
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# 
# =============================================================================
def main():
    
    
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
                                   13: start record and play back\n\
                                   14: ssh, process and send feedback\n\
                                   15: game time\n\
                                   please make selection: "))
        
# =============================================================================
        if taskNumber == 0:
#           Intro to entire session
            task = '0'
# =============================================================================
# =============================================================================
#       task 1: Start single note play without color
        elif taskNumber == 1:
            

            task = 'note'
        
# =============================================================================
#       task 2: Start single note play along with color  
        elif taskNumber == 2: 
            
           
            task = 'note+color'
        
# =============================================================================
#       task 3: Start multiple notes play along with color
        elif taskNumber == 3:
                
            
            task = 'notes+colors'
        
# =============================================================================
#       task 4: Start play whole song 
#       first half song
        elif taskNumber == 4:
            
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3]
            task = 'notes+color'
# =============================================================================
#       task 5: Start play whole song 
#       second half song 
        elif taskNumber == 5:
            
            keys = [0,0,1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0,
                    1,1,5,5,6,6,5,0,4,4,3,3,2,2,1,0]
            task = 'notes+color'

# =============================================================================
#       task 6: play the whole song
        elif taskNumber == 6:
            
            keys = [5,5,4,4,3,3,2,0,5,5,4,4,3,3,2,0]
            task = 'song'

# =============================================================================
# =============================================================================
#        task 14: shh, transfer file and ntft get frequency, then make judgement
#        send feedback to kid
        elif taskNumber == 14:
        
            try:
                with open(fileName, 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', 
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([task, keys, '122', '.667'])
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (fileName, filewriter.line_num, e))
# =============================================================================
            
        else:
            break
        
# =============================================================================
# Calling the main
if __name__ == "__main__":

    main()    
# =============================================================================
# End of the test session program