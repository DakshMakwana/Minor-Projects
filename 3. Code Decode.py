"""THIS PROGRAM IS DESIGNED TO CODE OR DECODE A MESSAGE as To code 
if word is of 2 character it will be reversed 
but if word is of greater than 2 characters 
then the first character goes to last character
and three random character are added to both end of word
And do vice-versa to decode"""

print("WELCOME TO MESSAGE CODE/DECODE PROGRAM")

import sys
import random
import string

words = input("enter the message: ").split()
a = int(input("enter 1 to code , -1 to decode & 0 to end: "))

word_list = []

if(a == 1):
    for word in words:
        r1 = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
        r2 = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
        if(len(word) >= 3):
            word = r1 + word[1:] + word[0] + r2
            word_list.append(word)
        else:
            word = word[::-1]
            word_list.append(word)
elif(a == -1):
    for word in words:
        if (len(word) >= 3):
            word = word[-4:-3] + word[3:-4]
            word_list.append(word)
        else:
            word = word[::-1]
            word_list.append(word)
else :
    print("process ended")
    sys.exit()
for word in word_list:
    print(word , end=" ")