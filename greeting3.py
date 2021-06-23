import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")
    date()
    time()
    hour  = datetime.datetime.now().hour
    
    if hour>=6 and hour <12:
        speak("Good morning")
    elif hour >= 12 and hour <18:
        speak("Good afternoon")
    elif hour >=18 and hour <20:
        speak("Good Evening")
    elif hour>=20 and hour <=24 :
        speak("Good night")
        
    speak("Pogo at your  service. How I can help you?")
wishme()

