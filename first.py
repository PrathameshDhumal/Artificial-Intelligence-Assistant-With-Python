import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150 
engine.setProperty('rate' , newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is Rambo")
