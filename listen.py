import speech_recognition
import speak
recognizer = speech_recognition.Recognizer()

def hear():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		speak.talk("")
	except speech_recognition.RequestError as e:
		print("Recog Error: {0}".format(e))

	return ""