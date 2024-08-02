import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)  
    engine.runAndWait()


def ProcessCommand(c):
    print(c)
    if c.lower() == "open facebook":
        webbrowser.open("https://www.facebook.com/")
        speak("Opening facebook")
    elif c.lower() == "open google":
        webbrowser.open("https://www.google.co.in/")
        speak("Opening google")
    elif c.lower() == "open youtube":
        webbrowser.open("https://www.youtube.com/")
        speak("Opening youtube")
    elif c.lower() == "open instagram":
        webbrowser.open("https://www.instagram.com/")
        speak("Opening instagram")
    elif c.lower() == "open twitter":
        webbrowser.open("https://www.twitter.com/")
        speak("Opening twitter")
    elif c.lower() == "open linkedin":
        webbrowser.open("https://www.linkedin.com/")
        speak("Opening linkedin")
    elif c.lower() == "open github":
        webbrowser.open("https://www.github.com/")
        speak("Opening github")
        
    pass


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
            audio = r.listen(source,timeout=2,phrase_time_limit=2)    
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