import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import os
import wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)  
    engine.runAndWait()

def ProcessCommand(c):
    print(c)
  
    if c.lower() == "open stackoverflow":
        webbrowser.open("https://www.stackoverflow.com/")
        speak("Opening stackoverflow")
    elif c.lower() == "open gmail":
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        speak("Opening gmail")
    elif c.lower() == "open music library":
        webbrowser.open("https://www.youtube.com/watch?v=ZZ5zTOpuR7o&list=LL")
        speak("Opening music library")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1:]
        song_name = " ".join(song)
        youtube_url = f"https://www.youtube.com/results?search_query={song_name}"
        webbrowser.open(youtube_url)
        speak(f"Playing {song_name} on YouTube")
    elif c.lower().startswith("open"):
        app = c.lower().split(" ")[1:]
        app_name = " ".join(app)
        webbrowser.open(f"https://www.{app_name}.com")
        speak(f"Opening {app_name}")
    elif c.lower().startswith("search"):
        search = c.lower().split(" ")[1:]
        search_name = " ".join(search)
        search_url = f"https://www.google.com/search?q={search_name}"
        webbrowser.open(search_url)
        speak(f"Searching {search_name} on Google")
    elif c.lower().startswith("run"):
        application = c.lower().split(" ")[1:]
        application_name = " ".join(application)
        subprocess.run(application_name)
        speak(f"Running {application_name}")
    elif c.lower().startswith("tell me about"):
        topic = c.lower().split(" ")[3:]
        topic_name = " ".join(topic)
        try:
            result = wikipedia.summary(topic_name, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("Sorry, I couldn't find any information on that topic.")

if __name__ =="__main__":
    speak("Initializing Jarvis")
while True:
    #Listen For The Wake Word Jarvis
    # obtain audio from the microphone
    r = sr.Recognizer()

    # recognize speech using Sphinx
    print("recognizing...")
    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source,timeout=2,phrase_time_limit=1)    
        word =r.recognize_google(audio)

        if (word.lower() == "jarvis"):
            speak("Yes sir?")

        #Listening to command
        with sr.Microphone() as source:
            print("Jarvis Active....")
            audio = r.listen(source)    
            command =r.recognize_google(audio)

            ProcessCommand(command)

    except Exception as e:
        print("Error; {0}".format(e))