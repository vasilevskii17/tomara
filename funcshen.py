import webbrowser
import subprocess
import pyttsx3
from pyttsx3 import Engine
import os
import sys
import samsungctl
from samsungctl import Remote
import speech_recognition as sr
import time


engine = pyttsx3.init()
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')


def speaker(text):
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://ya.ru/', new=2)
    print('загружаю яндекс ')


def youtub():
    webbrowser.open('https://youtube.com/', new=2)
    print('включаю ютубчик')


def passive():
    print('')


def game():
    webbrowser.open('https://yandex.ru/games/', new=2)
    print('играйте на здоровье')


def offBot():
    sys.exit()
    print('')


def weather():
    webbrowser.open('https://yandex.ru/pogoda/?lat=44.924183&lon=38.83749&utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home', new=2)
    print('')


def offpc():
    os.system('shutdown')
    print('пк выключен')


def samsung_off():
    tv = Remote('<IP>', 55000)
    tv.connect()
    #.power_on()
    tv.disconnect()


def samsung_on():
    config = {
        "name": "Samsung",
        "description": "Samsung TV Remote",
        "id": "<ID>",
        "port": 55000,
        "host": "<IP>",
        "timeout": 0,
    }


def film():
    webbrowser.open('https://yandex.ru/search/?text=фильмы+2023&lr=121361&clid=2349564&search_source=yaru_desktop_common', new=2)
    print('включаю фильмы')


def voice_search():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите ваш запрос...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language='ru-RU')
        print("Вы сказали: ", query)
        speaker("сейчас найду")

        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(search_url)
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError:
        print("Ошибка запроса к сервису распознавания речи")
