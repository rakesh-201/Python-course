import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")
    
def takeCommand():
    #IT TAKES MICROPHONE INPUT FROM THE USER AND GIVES STRING OUTPUT
    
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        print('done')
        speak('done')
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
        speak(f"User said:  {query}\n")
    except Exception as e:
        print("Say that again please......")
        speak("Say that again please......")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    speak("listening")
    while 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime("%Y:%m:%d")
            speak(strDate)
        elif 'open vscode' in query:
            codePath = r"C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'exit' in query:
            speak("Thank you Sir. Do call if need any Help.")
            exit()
    
