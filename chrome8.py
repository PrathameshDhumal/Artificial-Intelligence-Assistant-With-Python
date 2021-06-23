import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-US')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...") 
        
        return "None"
    return query
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("emailid@gmail.com","123")
    server.sendmail("xyz@gmail.com",to, content)
    server.close()

if __name__ == "__main__":
    
    wishme()
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query , sentences = 2 )
            speak(result)
        elif "send email" in query: 
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("The mail was sent sucessfully")
               
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("what should i search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
