#Artificial Intelligence Assistant (JARVIS) using Python Programming Language.


#Import statements 
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import wikipedia   #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui    #pip install pyautogui
import psutil   #pip install psutil
import pyjokes

#Start
#init
engine = pyttsx3.init()
#Voice Modification
def voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 150
    engine.setProperty('rate' , newVoiceRate)
    
#Funtion for speak text 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function to tell the current time   
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)

#Function to tell the present date
def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

#Funtion to Greet
def wishme():
    speak("Welcome back sir!")
   
    hour  = datetime.datetime.now().hour
    
    if hour >=6 and hour <=12:
        speak("Good morning")
    elif hour >= 12 and hour <18:
        speak("Good afternoon")
    elif hour >=18 and hour <24 :
        speak("Good Evening")
    else:
        speak("Good night")
    
      
    speak("Jarvis at your  service. How can i help you?")

#Function for use of microphone
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
        
        return "No input"
    return query

#Function to Send Email     
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("emailid@gmail.com","123")
    server.sendmail("xyz@gmail.com",to, content)
    server.close()

#Function to take Sceenshot of the window
def screenshot():
    img  = pyautogui.screenshot()
    img.save("ss.png")
 
#Function to tell CPU usage and Battery Percent 
def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at" + usage)
    
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    speak ("percent")
    
#Function to tell jokes
def jokes():
    speak(pyjokes.get_joke())

#Main Function   
if __name__ == "__main__":
    #Greeting
    voice()
    wishme()
    
    while True:
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "sleep" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", " ")
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

        elif "search in chrome" in query:############
            speak("what should i search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
            
        elif "logout" in query:
            os.system("shutdown - 1")
            
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            
        elif "restart" in query:
            os.system("shutdown /r /t 1")
            
        elif "play songs" in query : ##############
            songs_dir = "D:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir , songs[0]))
            
        elif "remember that" in query:
            speak ("What should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data) 
            remember= open("data.txt", "w")
            remember.write(data)
            remember.close()
            
        elif "do you know anything " in query:#############
            remember = open("data.txt","r")
            speak("you said me to remember that " + remember.read())
        
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken")
            
        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()
            
#End of program            