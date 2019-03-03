# -*- coding: utf-8 -*-
"""
Speech Recognition
"""
from naoqi import ALProxy
import time
import random
        
def onLoad(self):
    self.am = ALProxy("ALAutonomousMoves")
def onInput_onStart(self):
    self.am.setExpressiveListeningEnabled(False)
    # Ensure the robot does not move his hand back to the neutral position
    self.am.setBackgroundStrategy("none")



class SpeechRecognition:
    
    def __init__(self, IP, PORT, condition="psycho"):
        try:
            self.speechRecProxy = ALProxy("ALSpeechRecognition", IP, PORT)
            self.speechRecProxy.setParameter('Sensitivity',1)
            self.memoryProxy = ALProxy("ALMemory", IP, PORT)
            self.speakProxy = ALProxy("ALTextToSpeech", IP, PORT)
            self.am = ALProxy("ALAutonomousMoves",IP, PORT)

            print('Speech Recognition initialized')
        except Exception, e:
            print "Could not create proxy to ALSpeechRecognition"
            print "Error was: ", e
            
        try:
            self.speechRecProxy.unsubscribe("ASR")
        except:
            pass


        self.condition = condition
           
        self.speechRecProxy.setLanguage("English")
        self.vocabulary = [ "one", "two", "three", "four", "five", "six", "seven", 
                      "eight", "nine", "ten", "yes", "no"]
        self.speechRecProxy.setVocabulary(self.vocabulary, True)
        
        self.eventName = "ALSpeechRecognition/WordRecognized"
        self.wordSpotted = "ALSpeechRecognition/SpeechDetected"
        
        
    def stopmove(self):
        """
        stop automated life
        """
        self.am.setExpressiveListeningEnabled(False)
        self.am.setBackgroundStrategy("none")
        
    def introduce(self):
        """
        Introduction part of the experiment
        """

        self.stopmove()
        self.speakProxy.say("Hi, my name is Marvinus. What is your name?")
        self.speechRecProxy.subscribe("ASR")
        try:
            while not self.memoryProxy.getData("SpeechDetected"):
                pass
            while self.memoryProxy.getData("SpeechDetected"):
                pass
        except KeyboardInterrupt:
            self.speechRecProxy.unsubscribe("ASR")
            print "Interrupted by user"
            print "Stopping..."
            
        self.speechRecProxy.unsubscribe("ASR")
        self.stopmove()
        self.speakProxy.say("Nice to meet you! I love music and playing instruments is my hobby. Recently I started playing the metallophone. Actually, I have been practicing a few songs all day long. Let me play a few for you and you can tell me what you think! Please rate my performances with a grade between 1 and 10 with 1 being the worst and 10 the best grade!")
       
    def say_song(self, song):
        """
        Say the title of the song
        :param song: number of song in jukebox
        """
        time.sleep(2)
        self.speakProxy.say("The song I will play now is: {0}".format(song))
       
    def detroduce(self):
        """
        Have the robot say goodbye after the experiment
        """
        self.stopmove()
        self.speakProxy.say("Well, that were all the songs I know so far. Thank you for listening to them and rating my performance! I wish I could play some more, but I don't remember any others. Actually, I was in the middle of practising a new song when you came by, would you mind to leave me alone so I can practice some more?" )
        time.sleep(3)
        self.speakProxy.say("Thanks again for listening to my music, it was nice to meet you!")
        
    def start_recognition(self, last_song=False):
        """
        Start listening
        :param last_song: is the song the last song in the experiment?
        """
        
        number = self.confirm()
            
        print number
        self.react(number, last_song)

            
    def listen(self, array):
        """
        general function to detect spoken word out of list of words
        :param array: possible words
        :return: the recognized word
        """
        
        self.speechRecProxy.subscribe("ASR")
        recognized_word = ""
        while recognized_word == "":
            time.sleep(0.5)
            recognized_word = self.memoryProxy.getData("WordRecognized")
            recognized_word = recognized_word[0].replace("<...>", "")
            recognized_word = recognized_word.strip()
            print recognized_word
        self.speechRecProxy.unsubscribe("ASR")
        if recognized_word in array:
            return recognized_word
        else:
            self.stopmove()
            self.speakProxy.say("Could you repeat that please?")
            return self.listen(array)
            
    def confirm(self):
        """
        Was the recognized word correct? (Asks for confirmation from participant)
        :return: the recognized word
        """
        confirmed = ""
        recognized_word = ""
        self.speakProxy.say("Please rate my performance with a number between 1 and 10.")
        while confirmed != "yes":
            
            recognized_word = self.listen(self.vocabulary[:-2])
            self.stopmove()
            self.speakProxy.say("Did you say " + str(recognized_word) + "?")
            confirmed = self.listen(self.vocabulary[-2:])
            if confirmed == "no":
                self.stopmove()
                self.speakProxy.say("Oh I am so sorry. Please repeat your rating.")

        return recognized_word
        
    def react2(self, word):
        """
        Nao reacts to the rating
        :param word: rating
        """
        global reactions
        
        if self.condition == "social":
            if word == "one" or word =="two" or word == "three" :
                self.speakProxy.say("Was it that bad?")
            elif word == "four" or word == "five" or word == "six" or word == "seven":
              self.speakProxy.say("I will try better next time")
            elif word == "eight" or word == "nine":
                 self.speakProxy.say("You like that? Wait until you hear this one!")
            elif word == "ten":
                 self.speakProxy.say("I am so glad you liked it, I worked on this for several months. I am actually thinking of performing next month in theatre, would you come visit me?")
            else:
                self.speakProxy.say("I do not understand you. Could you repeat what you just said?")
        elif self.condition == "psycho":
            if word in self.vocabulary[:-2]:
                reaction = random.randint(0, len(reactions)-1)
                self.speakProxy.say(reactions[reaction])
            else:
                self.speakProxy.say("I do not understand you. Could you repeat what you just said?")
                
    def react(self, word, last_song=False):
        condition = self.condition
        lottery = random.randint(1,3)  
        self.stopmove()
        if not last_song:
            if condition != 'psycho':    
        
                if word == "one" or word =="two":
                    if lottery == 1:
                        self.speakProxy.say("You are making a joke, right? Please tell me that was a joke.")
                    elif lottery == 2:
                        self.speakProxy.say("I am a shame to my family.")
                    elif lottery == 3:
                        self.speakProxy.say("Well, you try to play a xylophone without proper hands.")
                elif word == "three" or word == "four":
                    if lottery == 1:
                        #self.speakProxy.say("I'm sorry it was that bad... I'll try harder for the next song!")
                        self.speakProxy.say("Maybe I should just stop playing. Can I try one other song?")
                    elif lottery == 2:
                        self.speakProxy.say("I know, I made so many mistakes. Please at least listen to one more.")
                    elif lottery == 3:
                        self.speakProxy.say("I am sorry I wasted your time. I hope I can make it up to you with the next song.")
                elif word == "five" or word == "six":
                    if lottery == 1:
                        self.speakProxy.say("I can't believe I still didn't get that right. Please, give me one more chance.")
                    elif lottery == 2:
                        self.speakProxy.say("This is so embarrassing, let me try again.")
                    elif lottery == 3:
                        self.speakProxy.say("Sorry, I forgot some of the notes. Can you endulge one more?")            
                elif word == "seven":
                    if lottery == 1:
                        self.speakProxy.say("The piece is a bit difficult for me, but I am glad you at least weren't completely unsatisfied. Hopefully you really enjoy the next song.")
                    elif lottery == 2:
                        self.speakProxy.say("Well a seven is a passing grade, but I hope I can do better than this.")
                    elif lottery == 3:    
                        self.speakProxy.say("I had hoped I did better, but it's better than nothing. One more time!")
                elif word == "eight":
                    if lottery == 1:
                        self.speakProxy.say("I am glad you kind of liked it! What about this next song? ")
                    elif lottery == 2:
                        self.speakProxy.say("I will be a professional one day! But I need to practice a lot more, so how about the next song?")
                    elif lottery == 3:
                        self.speakProxy.say("Wow, you gave me an eight! Now I'm even more motivated to show you the rest.")
                    
                elif word == "nine":
                    if lottery == 1:
                        self.speakProxy.say("You like that? Wait until you hear this one!")
                    elif lottery == 2:
                        self.speakProxy.say("This is my favourite piece as well! I hope I can do the next one just as well.")
                    elif lottery == 3:
                        self.speakProxy.say("I am so happy my efforts paid off and that you liked it so much! Maybe I can do even better for the next one.")
                elif word == "ten":
                    if lottery == 1:
                        self.speakProxy.say("I am so glad you liked it, I worked on this for several months. I am actually thinking of performing next month in theatre! Let me recite this next one as well.")
                    elif lottery == 2:
                        self.speakProxy.say("Wow, you are too kind! I am touched. I hope you like the next one just as much. ")
                    elif lottery == 3:
                        self.speakProxy.say("Was it that good? Maybe I will start composing my own songs! But first, I have another one to show you.")
            else:
                    if lottery == 1:
                        self.speakProxy.say("We will now continue." )
                    elif lottery == 2:
                        self.speakProxy.say("Okay, let me play another song.")
                    elif lottery == 3:
                        self.speakProxy.say("Beep...?")
                        time.sleep(0.4)
                        self.speakProxy.say("Boop!" )
                        self.speakProxy.say("This is my next song.")
        else:
            if condition != 'psycho':    
        
                if word == "one" or word =="two":        
                    self.speakProxy.say("You are making a joke, right? Please tell me that was a joke.")
                    self.speakProxy.say("Are you trying to make me sad? ")
                    self.speakProxy.say("Well, you try to play a xylophone without proper hands.")
                elif word == "three" or word == "four":
                    if lottery == 1:
                        self.speakProxy.say("I'm sorry it was that bad...")
                    elif lottery == 2:
                        self.speakProxy.say("I know, I made so many mistakes.")
                    elif lottery == 3:
                        self.speakProxy.say("I am sorry I wasted your time.")
                elif word == "five" or word == "six":
                    if lottery == 1:
                        self.speakProxy.say("Ah, still too many mistakes!")
                    elif lottery == 2:
                        self.speakProxy.say("This is so embarrassing.")
                    elif lottery == 3:
                        self.speakProxy.say("Sorry, I forgot some of the notes.")            
                elif word == "seven":
                    if lottery == 1:
                        self.speakProxy.say("The piece is a bit difficult for me, but I am glad you at least weren't completely unsatisfied.")
                    elif lottery == 2:
                        self.speakProxy.say("Well a it is a passing grade, but I hope I can do better than this.")
                    elif lottery == 3:    
                        self.speakProxy.say("I had hoped I did better, but it's better than nothing.")
                elif word == "eight":
                    if lottery == 1:
                        self.speakProxy.say("I am glad you kind of liked it!")
                    elif lottery == 2:
                        self.speakProxy.say("I will be a professional one day! But I need to practice a lot more.")
                    elif lottery == 3:
                        self.speakProxy.say("Wow, you gave me a eight!")
                    
                elif word == "nine":
                    if lottery == 1:
                        self.speakProxy.say("You like that?")
                    elif lottery == 2:
                        self.speakProxy.say("This is my favourite piece as well!")
                    elif lottery == 3:
                        self.speakProxy.say("I am so happy my efforts paid off and that you liked it so much!")
                elif word == "ten":
                    if lottery == 1:
                        self.speakProxy.say("I am so glad you liked it, I worked on this for several months. I am actually thinking of performing next month in theatre!")
                    elif lottery == 2:
                        self.speakProxy.say("Wow, you are too kind! I am touched.")
                    elif lottery == 3:
                        self.speakProxy.say("Was it that good? Maybe I will start composing my own songs!")
            else:
                    if lottery == 1:
                        self.speakProxy.say("We will now stop." )
                    elif lottery == 2:
                        self.speakProxy.say("Okay.")
                    elif lottery == 3:
                        self.speakProxy.say("Beep...?")
                        time.sleep(0.4)
                        self.speakProxy.say("Boop!" )
            
            
    def stop_recognition(self):
        self.speechRecProxy.unsubscribe("ASR")
