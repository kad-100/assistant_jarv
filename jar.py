import pyttsx3

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voice[0].id)

def speak(audio):

engine.say(audio) 

engine.runAndWait()
if __name__=="__main__" :

speak("Code With Kushagra")
import datetime

def wishme():

hour = int(datetime.datetime.now().hour)

import speechRecognition as sr

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
          try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
        return query

        if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() 

  
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
            elif 'open youtube' in query:
            webbrowser.open("youtube.com")

            elif 'open google' in query:
            webbrowser.open("google.com")

            elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
             elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
             elif 'open code' in query:
            codePath = "C:\\Users\\Kushagra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kushagradixitt@gmail.com', 'passwordispassword')
    server.sendmail('kushagradixitt@gmail.com', to, content)
    server.close()
    elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kushagrayourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
                
