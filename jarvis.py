import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5') # to take voices input
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    # Will speak the audio passed to the function
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # Will wish according to the time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may i help you")
        
        
def takeCommand():
    # It takes microphone input from the user and output is string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kunalmehndi10@gmail.com', 'Your-Password')
    server.send('kunalmehndi10@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()    
    while(True):
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            
        elif 'open leetcode' in query:
            speak("Opening Leetcode")
            webbrowser.open("leetcode.com")
            
        elif 'open codechef' in query:
            speak("Opening Codechef")
            webbrowser.open("codechef.com")
            
        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("gmail.com")
            
        elif 'open geeks for geeks' in query:
            speak("Opening GeeksforGeeks")
            webbrowser.open("geeksforgeeks.com")
            
        elif 'play music' in query:
            music_dir = 'H:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.random()*len(songs)]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VScode")
            os.startfile(codepath)
        elif 'open file' in query:
            wordpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening Word")
            os.startfile(wordpath)
        
        elif 'email to me' in query:
            try:
                speak("What should i Say ?")
                content = takeCommand()
                to = "kunalmehndi10@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry the email cant be sent")
                
        elif 'quit' in query:
            break
        elif 'bye' in query:
            break