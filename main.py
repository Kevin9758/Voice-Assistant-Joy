import speech_recognition as sr
import time
import webbrowser
import datetime
import calendar
import playsound
import os
import pyautogui
import random
from gtts import gTTS
from datetime import date,datetime





rec = sr.Recognizer()




# record audio for joy to listen to and interpret
def record_audio(ask = False):
    with sr.Microphone(2) as source:
        if ask:
            joy_speak(ask)
        audio = rec.listen(source)
        speech = ''
        try:
            speech = rec.recognize_google(audio)
        except sr.UnknownValueError:
            joy_speak('Sorry, I did not understand')
        except sr.RequestError:
            joy_speak('Sorry, my speech service is down')
        return speech


# have joy read text by cnverting text to audio with tts
def joy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


# commands and responses for joy
def response(speech):
    if 'what is your name' in speech:
        joy_speak('My name is Joy')

    if 'what time is it' in speech:
        joy_speak(datetime.now().strftime("%H:%M"))

    if "what is today's date"  in speech or "what day is today" in speech:
        joy_speak(str(date.today()))

    if 'what weekday is it' in speech:
        joy_speak(calendar.day_name[date.today().weekday()])

    if 'music' in speech:
        joy_speak('opening spotify')
        os.startfile(r"C:\Users\K\AppData\Roaming\Spotify\Spotify.exe")

    if 'play' in speech or 'pause' in speech:
        pyautogui.press('playpause')

    if 'skip' in speech:
        pyautogui.press('nexttrack')

    if 'previous' in speech:
        pyautogui.press('prevtrack',2)

    if 'volume up' in speech:
        pyautogui.press('volumeup')

    if 'volume down' in speech:
        pyautogui.press('volumedown')

    if 'search' in speech:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        joy_speak('Here is what I found for ' + search)

    if 'find location' in speech:
        location = record_audio('What location would you like to find?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        joy_speak('Here is the location of ' + location)

    if 'thank you' in speech or 'thanks' in speech:
        joy_speak("you're welcome")
        exit()

    if 'goodbye' in speech or 'bye' in speech or 'exit' in speech or 'quit' in speech:
        joy_speak("Goodbye")
        exit()



time.sleep(1)
joy_speak('Hi, How can I help you?')
while 1:
    speech = record_audio()
    response(speech)





# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


