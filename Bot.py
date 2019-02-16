import tracy as t
import re
import speak
import listen

def reply(message):
    # Get the bot's response to the message
    response = t.respond(message)
    return response

speak.talk("Hi! I'm Tracy, your personal assistant, at your service.")
speak.talk("Before we start, what's your name?")
user = input("Name: ")
speak.talk("Nice to meet you, {0}".format(user))
count = 0
while True:
    text = listen.hear()
    if text == "":
        count += 1
        if count == 5:
            speak.talk("Would you like to talk to me about something?")
            text = listen.hear()
            if text == "no":
               count = 7
        if count == 7:
            speak.talk("Going to sleep")
            exit()
        continue
    print(user+": "+text)
    count = 0
    speak.talk(reply(text))
    if re.match(r'(shut(\s*)down+|good(\s*)night+|bye+)(.*)', text) is not None:
        exit()
