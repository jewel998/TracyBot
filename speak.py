import pyttsx3
import sys

if sys.platform == "win32":
	speech_engine = pyttsx3.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
	speech_engine.setProperty('rate', 150)
	speech_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
else:
	speech_engine = pyttsx3.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
	speech_engine.setProperty('rate', 150)

def talk(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

def talk_fast():
	speech_engine.setProperty('rate', 200)

def talk_normal():
	speech_engine.setProperty('rate', 150)