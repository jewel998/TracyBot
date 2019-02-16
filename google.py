import urllib
from bs4 import BeautifulSoup
import requests
import re
import speak
import listen
import nltk

text = "happiness"
def search(text):
    sentence = ""
    text = urllib.parse.quote_plus(text)
    url = 'https://google.com/search?q=' + text
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.prettify()
    speak.talk("Top {0} results processed from google".format(str(len(soup.find_all(class_='g')))))
    for g in soup.find_all(class_='g'):
        nltk_tokens = nltk.sent_tokenize(g.text)
        for tokens in nltk_tokens:
            sentence = sentence+tokens+"\n"
        string = re.sub(re.compile("/.[\s]",re.DOTALL ) ,"," ,sentence)
        print(string)
        speak.talk_fast()
        speak.talk(string)
        speak.talk_normal()
        sentence = ""
        speak.talk("Do you want to read the next result?")
        text = listen.hear()
        if text == "" or text == "no":
            return "Okay"
    return "Search something else?"
if __name__ == '__main__':
    search(text)
