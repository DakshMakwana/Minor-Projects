""" Write a python program which reminds you of drinking water every hour or two.
    Your program can either send desktop or beep notification for a specific OS """

# import time
# from plyer import notification
# import win32com.client as win

# speaker = win.Dispatch("SAPI.SpVoice")

# i = 1
# while i <= 24:
#     time.sleep(3600)
#     notification.notify(
#         title = "Alert!",
#         message = "This is remainder for you to drink water",
#         app_name = "Drink Water Remainder",
#         timeout = 10
#     )
#     for r in range(3):
#         speaker.speak("remainder to drink water")
#     i += 1


# # above one was for a notification and sound now we write a program for only a beep

import time
import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

i = 1
while i <= 24:
    time.sleep(3600)
    for r in range(3):
        speaker.speak("remainder to drink water")
    i += 1

### both these system are made to work 24 hour only if you wanted to run it always just comment out "i += 1"