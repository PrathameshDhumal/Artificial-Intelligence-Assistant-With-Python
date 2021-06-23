import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 135
engine.setProperty('rate' , newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is Rambo")
