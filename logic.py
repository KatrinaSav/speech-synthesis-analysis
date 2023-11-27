import pyttsx3
import requests
import webbrowser







from datetime import datetime
import speech_recognition as sr
from bs4 import BeautifulSoup


def text_to_speech(text, voice_str, rate_str, volume_str):
    engine = pyttsx3.init()

    voice_dict = {'Male': 2, 'Female': 1}
    voices = engine.getProperty('voices')
    voice = voices[voice_dict[voice_str]].id
    engine.setProperty('voice', voice)

    rate = 150
    volume = 0.5

    rate_volume_dic = {'Fast': 2, 'Default': 1 , 'Slow': 0.5}

    rate = rate * rate_volume_dic[rate_str]
    engine.setProperty('rate', rate)

    volume = volume * rate_volume_dic[volume_str]
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def recognize_speech(text):
    result = ""
    recognizer = sr.Recognizer()
    # names = sr.Microphone.list_microphone_names()
    # for n in names:
    #     print(n)
    with sr.Microphone(device_index=1) as source:
        print('Listeting...')
        audio = recognizer.listen(source)


    try:


        out_text = recognizer.recognize_google(audio, language='en-US')

        out_text = out_text.lower()
        rez = "no information"
        if "mona lisa" in out_text:
            rez = "The Mona Lisa bears a strong resemblance to many Renaissance depictions of the Virgin Mary, who was at that time seen as an ideal for womanhood. "

        elif 'sunflowers' in out_text:
            rez = "Sunflowers is the title of two series of still life paintings by the Dutch painter Vincent van Gogh."

        elif "black square" in out_text:
            rez = "Black Square is an iconic 1915 painting by Kazimir Malevich. The first version was done in 1915. "

        elif 'scream' in out_text:
            rez = "The Scream is a composition created by Norwegian artist Edvard Munch in 1893. The agonized face in the painting has become one of the most iconic images of art, seen as symbolizing the anxiety of the human condition. "

        elif 'last supper' in out_text:
            rez = "The Last Supper is a mural painting by the Italian High Renaissance artist Leonardo da Vinci, dated to 1495–1498. "

        if "voice" in out_text:
            print('TUT')
            text_to_speech(rez, 'Male', 'Default', 'Default')
            result = out_text + " : "+rez
        elif "find" in out_text:
            out_text.replace("find", "")
            r = requests.get('https://www.google.com/search?q={}'.format(out_text))
            soup = BeautifulSoup(r.text, 'html.parser')
            first_link = soup.find('div', class_='kCrYT').a['href']
            print(first_link)
            ind = len(first_link)-1
            ind = first_link.index('&')
            webbrowser.open(first_link[7:ind], new =2)
            result = out_text
        elif "text" in out_text:
            result = rez
        else:
            result = "No such command: " + out_text
    except Exception as e:
        result = "Error!"
        print(e)
    return result