import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #pre-installed
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os #pre-installed 
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import keyboard #pip install keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Gets the audio to be spoken as argument and speaks it out"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Wishes the user based on the current timings"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir!')
    elif hour>=12 and hour<18:
        speak('Good afternoon Sir!')
    else:
        speak('Good Evening Sir')

    speak('Jarvis System Initialized! How may I help you Sir?')

def takeCommand():
    """It takes microphone input and returns string output."""

    command = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing....")
        query = command.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'search' in query:
            speak("Searching Wikipedia...")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
