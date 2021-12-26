import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import subprocess
import ctypes
import pywhatkit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print('please  say that again')
        return "None"
    return query

def send_mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',smtplib.SMTP_PORT)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail before writing the below code since for logging in we should do this
    server.login('your email id','password')
    server.sendmail('your email',to,content)
    server.close()


if __name__ =='__main__':
    wish_me()
    speak('hello rocky how can I help you')

    while True:
        query=take_command().lower()

        if 'wikipedia' in query:
            print('Searching in wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)
            #print(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackverflow.com')

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
        elif 'play music' in query or 'play songs' in query:
            music_dir='C:\\Users\\Moturu Tarun Venkat\\Desktop\\songs'
            songslist=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songslist[0]))

        elif 'send mail' in query or 'send email' in query:
            
            try:
                speak('To whom you want to send')
                to=take_command() #or we can directly take to address as input 
                speak('what you want to send')
                content=take_command()
                send_mail(to,content)
                speak('Email sent successfully')
            except Exception as e:
                print(e)
                speak('Sorry Iam unable to send mail')

        #elif 'shutdown' in query:
            #os.system('shutdown/s/t 1')

        elif 'shutdown' in query:
            speak('Your system is going to be shutting down')
            subprocess.call('shutdown/p/f')

        #elif 'restart' in query:
            #os.system('shutdown/r/t ')
        elif 'restart' in query:
            speak('Restarting your system')
            subprocess.call(['shutdown','/r'])

        elif 'lock window' in query:
            speak('locking the device')
            ctypes.windll.user32.LockWorkStation()

        elif 'stop listening' in query or 'dont listen' in query:
            speak('For how much time should i dont listen')
            t=int(take_command())
            time.sleep(t)

        elif  'search' in query:
            query=query.replace('search','')
            webbrowser.open(query)
        #this requires stable internet connection and microphone should be good otherwise it wont recognize
        elif 'send whatsapp message' in query:
            try:
                speak('For whom you want to send')
                number='+919390190599'
                speak('What you want to send')
                msg=take_command()
                speak('Please specify the hour')
                hour=int(take_command())
                speak('Please specify the minute')
                min=int(take_command())
                pywhatkit.sendwhatmsg(number,msg,hour,min)
            except Exception as e:
                print(e)
                speak('Sorry Rocky unbale to send message')

        elif 'exit' in query or 'quit' in query or 'close' in query:
            speak('Thanks for using me Bye rocky ts')
            exit()




        

        