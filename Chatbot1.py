import string
import re
import random
import datetime
import time
import webbrowser
import sys
import platform
import json
import requests

os=platform.system()
date = []
today = str(datetime.date.today())
date.append(today)
localtime = time.asctime( time.localtime(time.time()) )
value = 0
songs = ["Freaky Friday-Lil Dicky ft.Chris Brown","Delicate-Taylor Swift"]
food = ["Sambhar","Idli","Dosa"]

class Tracy:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)

#-------------------
#For Opening Chrome
#-------------------
  def openbrowser(value):
    if value==0:
      return "Ok!"
    else:
      print("Enter the Url:")
      url=input('> ')
      if os == "Windows":
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
      elif os == "Linux":
        chrome_path = '/usr/bin/google-chrome %s'
      elif os == "MacOs":
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
      webbrowser.get(chrome_path).open(url)
      return "Done!"
#-------------------
#Google Search
#-------------------
  def search(value):
    if value==0:
      return "Ok!"
    else:
      print("What do you want to search online?")
      searchfor = input('> ')
      url="https://google.com/search?q="
      searchfor = url+searchfor
      if os == "Windows":
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
      elif os == "Linux":
        chrome_path = '/usr/bin/google-chrome %s'
      elif os == "MacOs":
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
      webbrowser.get(chrome_path).open(searchfor)
      return "Done!"
#--------------------
#For IP
#--------------------
  def mypublicip():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    print("Your IP is: {0}".format(j['ip']))
    return
#---------------------
#For Location
#---------------------
  def location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    print("Country Name:{0}".format(j['country_name'])+"\nCity:{0}".format(j['city'])+"\nLatitude & Longitude: [{0}".format(lat)+",{0}".format(lon)+"]")
    return

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = resp.find('%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.
#----------------------------------------------------------------------
gPats = [
  [r'Hi(.*)',
  ["what's up?","'sup?","sup","'sup","what's up!","what's up"]],

  [r'Hey(.*)',
  ["what's up?","'sup?","sup","'sup","what's up!","what's up"]],

  [r'What(.*) your name(.*)',
  ["I go by Tracy!", "My name is Tracita Stephani Lepcha!", "You can call me Tracy"]],

  [r'(.*)today(.*)date(.*)',
  ["Today's date is: {0}".format(date[0])]],

  ['How are you?',
  ["Great!","Sad!","I'm fine","Fine","Good"]],

  ["Tell me(.*)joke(.*)",
  ["A man asks a farmer near a field, \"Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.\"\nThe farmer says, \"Sure, go right ahead. And if my bull sees you, you'll even catch the 4:11 one.",
   "What is the difference between a snowman and a snowwoman?\n-Snowballs.",
   "\"You da bomb!\"\n\n\"No, you da bomb!\"\n\nIn America - a compliment. In the Middle East - an argument.",
   "\"I wasn't that drunk yesterday.\" \"Oh boy you took the shower head in your arms and told it to stop crying.\""]],


  ["What are you doing?",
  ["Chatting",
   "Nothing Much",
   "Have you heard the song {0}".format(random.choice(songs))]],

  ["Why are you sad?",
  ["We had {0} again!".format(random.choice(food))]],

  [r'(.*)google (.*)',
  ["Try \"Google this\" or \"Search Online\""]],
 
  [r'(.*)search(.*)online(.*)',
  ["Try \"Google this\" or \"Search Online\""]],
 
  [r'What(.*)time(.*)',
  ["The time is: {0}".format(localtime)]],

  [r'Open(.*)browser(.*)',
  ["Try \"Open browser\""]],

  [r'I need (.*)',
  [  "Why do you need %1?",
    "Would it really help you to get %1?",
    "Are you sure you need %1?"]],

  [r'Why don\'?t you ([^\?]*)\??',
  [  "Do you really think I don't %1?",
    "Perhaps eventually I will %1.",
    "Do you really want me to %1?"]],

  [r'Why can\'?t I ([^\?]*)\??',
  [  "Do you think you should be able to %1?",
    "If you could %1, what would you do?",
    "I don't know -- why can't you %1?",
    "Have you really tried?"]],

  [r'I can\'?t (.*)',
  [  "How do you know you can't %1?",
    "Perhaps you could %1 if you tried.",
    "What would it take for you to %1?"]],

  [r'I am (.*)',
  [  "Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?"]],

  [r'I\'?m (.*)',
  [  "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?"]],

  [r'Are you ([^\?]*)\??',
  [  "Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?"]],

  [r'What (.*)',
  [  "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?"]],

  [r'How (.*)',
  [  "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?"]],

  [r'Because (.*)',
  [  "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?"]],

  [r'(.*) sorry (.*)',
  [  "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?"]],

  [r'Hello(.*)',
  [  "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?"]],

  [r'I think (.*)',
  [  "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?"]],

  [r'(.*) friend (.*)',
  [  "Tell me more about your friends.",
    "When you think of a friend, what comes to mind?",
    "Why don't you tell me about a childhood friend?"]],

  [r'Yes',
  [  "You seem quite sure.",
    "OK, but can you elaborate a bit?"]],

  [r'(.*) computer(.*)',
  [  "Are you really talking about me?",
    "Does it seem strange to talk to a computer?",
    "How do computers make you feel?",
    "Do you feel threatened by computers?"]],

  [r'Is it (.*)',
  [  "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1."]],

  [r'It is (.*)',
  [  "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?"]],

  [r'Can you ([^\?]*)\??',
  [  "What makes you think I can't %1?",
    "If I could %1, then what?",
    "Why do you ask if I can %1?"]],

  [r'Can I ([^\?]*)\??',
  [  "Perhaps you don't want to %1.",
    "Do you want to be able to %1?",
    "If you could %1, would you?"]],

  [r'You are (.*)',
  [  "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?"]],

  [r'You\'?re (.*)',
  [  "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?"]],

  [r'I don\'?t (.*)',
  [  "Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?"]],

  [r'I feel (.*)',
  [  "Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?"]],

  [r'I have (.*)',
  [  "Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?"]],

  [r'I would (.*)',
  [  "Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?"]],

  [r'Is there (.*)',
  [  "Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?"]],

  [r'My (.*)',
  [  "I see, your %1.",
    "Why do you say that your %1?",
    "When your %1, how do you feel?"]],

  [r'You (.*)',
  [  "We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I %1?"]],

  [r'Why (.*)',
  [  "Why don't you tell me the reason why %1?",
    "Why do you think %1?" ]],

  [r'I want (.*)',
  [  "What would it mean to you if you got %1?",
    "Why do you want %1?",
    "What would you do if you got %1?",
    "If you got %1, then what would you do?"]],

  [r'(.*) mother(.*)',
  [  "Tell me more about your mother.",
    "What was your relationship with your mother like?",
    "How do you feel about your mother?",
    "How does this relate to your feelings today?",
    "Good family relations are important."]],

  [r'(.*) father(.*)',
  [  "Tell me more about your father.",
    "How did your father make you feel?",
    "How do you feel about your father?",
    "Does your relationship with your father relate to your feelings today?",
    "Do you have trouble showing affection with your family?"]],

  [r'(.*) child(.*)',
  [  "Did you have close friends as a child?",
    "What is your favorite childhood memory?",
    "Do you remember any dreams or nightmares from childhood?",
    "Did the other children sometimes tease you?",
    "How do you think your childhood experiences relate to your feelings today?"]],

  [r'(.*)\?',
  [  "Why do you ask that?",
    "Please consider whether you can answer your own question.",
    "Perhaps the answer lies within yourself?",
    "Why don't you tell me?"]],

  [r'quit',
  [  "Thank you for talking with me.",
    "Good-bye.",
    "Thank you, that will be $150.  Have a good day!"]],

  ['help',
  [  "\n\tTell me a joke - for hearing a joke\n\n\tMy IP - for your Public IP *\n\n\tMy Location - for your location *\n\n\tOpen browser - for opening chrome\n\n\tSearch Online / Google this - for google search *\n\n\t* requires Internet Connection"]],

  [r'(.*)',
  [  "Please tell me more.",
    "Let's change focus a bit... Tell me about your family.",
    "Can you elaborate on that?",
    "Why do you say that %1?",
    "Cool!",
    "Would you like to hear a joke?",
    "I see.",
    "Very interesting.",
    "%1?",
    "Sad Life!",
    "I see.  And what does that tell you?",
    "How does that make you feel?",
    "How do you feel when you say that?"]]
  ]

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  print('Friend\n---------')
  print('Talk to the program by typing in plain English, using normal upper-')
  print('and lower-case letters and punctuation.  Enter "quit" when done.')
  print('A few operations are case sensitive like \"Search Online\" or \"Open browser\"-')
  print('make sure to look after them')
  print('Type "help" for operations') 
  print('='*72)
  print('Hello.  How are you feeling today?')
  global value
  value = 1
  s = ''
  friend = Tracy();
  while s != 'quit':
    try:
      s = input('> ')
    except EOFError:
      s = 'quit'
#   print(s)
    if s == "Open browser":
      Tracy.openbrowser(value)
      continue
    if s == "Google this" or s == "Search Online":
      Tracy.search(value)
      continue
    if s == "clear":
      sys.stdout.flush()
      continue
    if s == "My IP":
      Tracy.mypublicip()
      continue
    if s == "My Location":
      Tracy.location()
      continue
#   while s in '!.':
#     s = s[:-1]
    print(friend.respond(s))


if __name__ == "__main__":
  command_interface()