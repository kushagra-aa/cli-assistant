import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    '''
    This Function takes a string and makes the audio engine speak the string
    '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''
    This Function wishes the user according to the current time
    '''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Morning,')

    elif hour>=12 and hour<18:
        speak('Noon,')

    elif hour>=18 and hour<21:
        speak('Evening,')

    else:
        speak('Night,')

    speak("Welcome Master")
    speak('Myself sasta jarvis')

def takeCommand():
    '''
    Function to take voice command
    from user mic and returns string
    '''
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('listening to user...')
        r.pause_threshold=1
        # energy_threshold for required loudness
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query= r.recognize_google(audio,Language='en-in')
    except Exception as e:
        print('Say that again please')
        return 'None'
    return query

if __name__ == '__main__':
    '''
    Main Function, this runs at the very first
    '''
    wishMe()
    while True:
        query=takeCommand().lower()
        
        # taks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentence=2)
            speak('According to Wikipedia')
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music'or'open spotify' in query:
            path="C:\\Users\\ACER\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(path)
        elif 'open vscode'in query:
            path="C:\\Users\\ACER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open figma' in query:
            path="C:\\Users\\ACER\\AppData\\Local\\Figma\\Figma.exe"
            os.startfile(path)
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
        elif 'the date' in query:
            strTime=datetime.datetime.now().date()
