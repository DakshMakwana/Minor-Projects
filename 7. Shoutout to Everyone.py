"""write a program to pronounce list of names using win32 API 
   if you are given a list l as follows
   l = ["rahul" , "nishant" , "harry"]"""

# piwin32 package

import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

l = ["rahul" , "nishant" , "harry" , "all of you guys"]

for i in l:
    command = f"Shoutout to {i}"
    speaker.rate = 0                    # speed of the audio [-10,10]
    speaker.volume = 50                 # volume of the audio [0,100]
    speaker.speak(command)
