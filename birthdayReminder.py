import time
import os 
import sys
import datefinder
import NERTagger
import listen
import speak

if sys.platform == "win32":
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
# Birthday file is the one in which the actual birthdays 
# and dates are present. This file can be  
# manually edited or can be automated.  
# For simplicity, we will edit it manually. 
# Birthdays should be written in this file in 
# the format: "MonthDay Name Surname" (Without Quotes) 
  
birthdayFile = 'data/birthday.data'

text = "set a reminder for february three for Jameson Singh"

def checkTodaysBirthdays(): 
    fileName = open(birthdayFile, 'r') 
    today = time.strftime('%m%d') 
    flag = 0
    speak.talk("Today's Birthdays")
    for line in fileName: 
        if today in line: 
            line = line.split(' ') 
            flag =1
            speak.talk("{0}".format(" ".join(line[1:])))
            if sys.platform == "win32":
                toaster.show_toast("Birthday Notifier","Birthdays Today: {0}".format(" ".join(line[1:])),threaded=True)
            else:
                os.system('notify-send "Birthdays Today: {0}"'.format(" ".join(line[1:]))) 
            while toaster.notification_active(): time.sleep(0.1)
    if flag == 0:
        speak.talk("no one special today")
        if sys.platform == "win32":
            toaster.show_toast("Birthday Notifier","No Birthdays Today!",threaded=True) 
        else:
            os.system('notify-send "No Birthdays Today!"') 
    return "Notification Removed"

def addBirthdays(text):
    matches = datefinder.find_dates(text)
    for match in matches:
        date = match.strftime('%m%d')
    names = NERTagger.get_names(text)
    if not date:
        speak.talk("Date: ")
        date = listen.hear()
        matches = datefinder.find_dates(text)
        for match in matches:
            date = match.strftime('%m%d')
    if not names:
        speak.talk("Reason for reminder: ")
        bname = listen.hear()
    else:
        bname = names[0]
    fileName = open(birthdayFile, 'a')
    fileName.write("\n"+date+" "+bname)
    fileName.close()
    return "Reminder is set"
  
if __name__ == '__main__': 
    addBirthdays(text)
    checkTodaysBirthdays() 