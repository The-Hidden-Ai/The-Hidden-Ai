import time
import pyttsx3
#======================
#Making The Hidden Ai
#======================
#The Hidden Ai
#1 Speaking
#2 Listening
#3 Watching
#5 Doing
#==============================================
#===[Hidden Ai]===
number = [1,2,3,4,5,6,7,8,9,0]
alphabet = ["a","b","c","d","e","f","g","h"]
#===============================================
creator = "The Hidden Ai " \
          "Made by Ashutosh kumar gautam"
#================================================
#=====[Speaking function]========================
# initialisation
engine = pyttsx3.init()
# Speaking Now...
engine.say("Welcome My name is Hidden Ai")
#closing
engine.runAndWait()
#finish
#================================================
