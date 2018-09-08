import re
import random

userlet = input('insert an english letter: ').lower()
corlet = random.randint(1,26)
#print(corlet)    
i = 0
while i != corlet:
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for a in alph:
        i+=1
        if a == userlet:
            break
    if i in (1,26):
    #print(i)
        if ((i <= 26):
            print('the correct letter stands to the left')
            userlet = input('insert an english letter: ').lower()
            i = 0
        elif i < corlet:
            print('the correct letter stands to the right')
            userlet = input('insert an english letter: ').lower()
            i = 0
        else:
            print('congrats on guessing the letter, smartass')
    else: 
