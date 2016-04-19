 #-*-coding:cp949
# 한글로 입력 방법 Help ->  FInd action -> Search "project encoding" -> Change encoding "X-window-949"
from sys import argv

script, user_name = argv # I wrote user_nav and use argv "kyongmook" // 스크랩트 파라만타
prompt = ">" #this shows " > " of a answer line front

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions")
print ("Do you like me %s?" % user_name)
likes = raw_input(prompt)

print(" Where do you I live %s?" % user_name)
lives = raw_input(prompt)

print ("What kind of computer do you have?")
computer = raw_input()

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer))

