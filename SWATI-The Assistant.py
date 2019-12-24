import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import time
import threading
import re
import pyautogui
import pygetwindow
import PySimpleGUI as sg
from timer import timer1
import cv2
from better_profanity import profanity
from playsound import playsound 
from datetime import date
from sound import Sound
import wmi









engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('H6XWLV-465H93W4A4')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('Lisa: ' + audio)
    window.refresh()
    window['_OUTPUT1_'].update(audio)
    window.refresh()
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    playsound('C:/Users/USER/Downloads/Telegram Desktop/SVATI/communication-channel.mp3')
    speak('Starting all system applications. Installing all drivers! Calibrating and examing all the core processors')
    playsound('C:/Users/USER/Downloads/Telegram Desktop/SVATI/Computer_Start-Up-Your_Mom-1280862923.mp3')
    speak('All systems have been started')
    speak('Now i am all in mine')
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        window['_OUTPUT1_'].update("Listening...")
        window.refresh()
        # r.pause_threshold =  1
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! ')
        query = myCommand()
        print(query)


    return query


def timer(self, timerr):
    timerr = int(timerr)
    time.sleep(timerr)
    speak('Time up')

def main_process():
        window.refresh()
        query = myCommand();
        query = query.lower()
        window['_OUTPUT_'].update(query)
        window.refresh()
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'youtube' in query:
            query=query.lstrip("search")
            query=query.rstrip("on youtube")
            speak('okay')
            webbrowser.open("http://www.youtube.com/results?search_query=" + ''.join(query))

        elif 'google map' in query:
            query=query.lstrip("search")
            query=query.rstrip("on google map")
            speak("Okay sir")
            webbrowser.open("https://www.google.com/maps/search/"+''.join(query))

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'google' in query:
            reg_ex = re.search('search (.+)', query)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'http://www.google.co.in/search?q=' + domain
                webbrowser.open(url)
            '''query=query.lstrip("search")
            query=query.rstrip("on google")
            speak('okay')
            webbrowser.open('http://www.google.co.in/search?q=' + ''.join(query))'''

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'close current tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'restore recent tab' in query:
            pyautogui.hotkey('ctrl','shift','t')


        elif 'system shutdown' in query:
            os.system("shutdown /s /t 1")
            speak("Bye Sir!")

        elif 'system restart' in query:
            os.system("shutdown /r /t 1")
            speak("Bye Sir!")

        elif 'will you be my girlfriend' in query:
            speak("sorry i have a boyfriend better then you")

        



        

        elif 'brightness' in query:
            brightness = query.lstrip("set brightness to")
            brightness = brightness.rstrip("%")
            bright=int(brightness)
            brightness = bright # percentage [0-100]
            c = wmi.WMI(namespace='wmi')
            methods = c.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(brightness, 0)

        elif 'volume' in query:
            volume = query.lstrip("set volume to")
            volume = volume.rstrip("%")
            volume=int(volume)
            Sound.volume_set(volume)

        elif 'mute' in query:
            Sound.mute()










        elif 'close all' in query:
            pyautogui.hotkey('alt','f4')

        elif 'new tab' in query:
            pyautogui.hotkey('ctrl','t')


        elif 'save' in query:
            pyautogui.hotkey('ctrl','s')

        elif 'switch tab' in query:
            pyautogui.hotkey('ctrl','tab')




        

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!','I am feeling good! If i was any better, vitamins would be taking me', 'I am fine!', 'Nice!', 'I am nice and full of energy','great, thanks','feeling like a lean, mean, assisting machine','For computer software i say i am preety good','its been a good day, thanks for asking, I am busy learning a bunch of languages,actually']


            speak(random.choice(stMsgs))


        elif 'open command prompt' in query:
            os.system('start cmd')

        



        elif 'are you boy or girl' in query:
            msg=['i try to stay neutral','well, althrough my voice sounds female! I am actually AI. so I am neither! creazy hmmm?']
            speak(random.choice(msg))

        elif 'are you better than alexa'  in query:
            msg=['i couldnt compare to myself to Alexa. assistant have to stick together','I like Alexa\'s blue light. her voice is nice too']
            speak(random.choice(msg))

        elif 'are you better than siri' in query:
            msg=['it\'s hard to compare, we\'re like apples and oranges, because Siri works for Apple and I like oranges','We\'re diffrent ketties of fish','siri is my senior, i am on developing stage']
            speak(random.choice(msg))

        elif 'are you better than cortana' in query:
            msg['Full respect. Being an assistant isn\'t easy','She seems nice']
            speak(random.choice(msg))

        elif 'who is your favourite superhero' in query:
            msg=['my superheroes are the one how made me, because without them i am nothing','I\'ve always thought of teachers as heroes, getting vital information to the world\'s youth in a single bound']
            speak(random.choice(msg))

        elif 'Do you love anyone' in query:
            speak('the only thing i am really feeling a strong connection to is wi-fi')

        elif 'abba harmonium bajate the' in query:
            speak("nahi, abba harmonium khate the, abee saaaleeee!, maaf karna gusse me idhar udhar nikal jati hun.")

        

        



        elif 'do you ever get tired' in query:
            msg=['I don’t exactly need to grab 40 winks, but I suppose this device does need to be plugged in occasionally.','it would be impossible to tire of our conversation!','I might need to charge my processor occasionally. But i dont ever have to go to the land of nod','']
            speak(random.choice(msg))
        elif "screenshot" in query:
            pyautogui.screenshot("scrshot.png")

        elif 'selfie' in query:
            query=query.lstrip("let\'s take a")
            query=query.rstrip("selfie")
            speak('okay')

            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0

            while True:
                ret, frame = cam.read()
                cv2.imshow("test", frame)
                if not ret:
                    break
                k = cv2.waitKey(1)

                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()

            cv2.destroyAllWindows()

        elif 'type' in query:
            speak('Please place the cursor where you want to type.')
            speak('Tell me what to type')
            pyautogui.typewrite(myCommand())

        elif 'select all' in query:

            pyautogui.hotkey('ctrl', 'a')


        elif 'copy' in query:
            pyautogui.hotkey('ctrl','c')
        elif 'cut' in query:
            pyautogui.hotkey('ctrl','x')

        elif 'paste' in query:
            pyautogui.hotkey('ctrl', 'v')

        elif 'close current window' in query:
            pyautogui.hotkey('ctrl' , 'w')
        elif 'close all' in query:
            pyautogui.hotkey('alt','f4')
            


        elif 'scroll down' in query:
            pyautogui.scroll(-500)

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'myself' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("jaanichauhan0@gmail.com", '7073180849')
                    server.sendmail('shadabhussain007khan@gmail.com', "shadabhussain007khan@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'headlines' in query:
            import requests
            url = ('https://newsapi.org/v2/top-headlines?'
                   'country=in&'
                   'apiKey=250510cf5a29477b813d8e7884f777cc')
            response = requests.get(url)
            print(type(response.json()))
            print(response.json())

        elif 'timer' in query:
            timer_time = query.lstrip("set timer for")
            timer_time = timer_time.rstrip("minutes")
            timerr=int(timer_time)

            timerr=timerr*60
            #print(timerr)
            timer1(timerr)


        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()


        elif 'what is your name' in query:
            speak('My name is swati and i am a AI based personal assistant')


        elif 'how old are you' in query:
            speak('I am 1 year and 2 months old')







        elif 'play music' in query:
            music_dir = 'C:/Users/USER/Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        



        # elif 'play music' in query:
        # music_folder = path
        # music = [music1, music2, music3, music4, music5]
        # random_music = music_folder + random.choice(music) + '.mp3'
        # os.system(random_music)

        # speak('Okay, here is your music! Enjoy!')'''

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                speak('I didnt get that please say again')

        speak('Next Command! Sir!')

layout = [[sg.Image(r'ai.png'), sg.Text('Input:'), sg.Text('', size=(50,2), key='_OUTPUT1_')],
          [sg.Text('Output:'),sg.Text('', size=(50,2), key='_OUTPUT_'), sg.Image(r'hi.png')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, no_titlebar='true',grab_anywhere='true')

while True:  # Event Loop
    event, values = window.read()       # can also be written as event, values = window()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        #wake_word=['hey google','activate jarvis','listen']
        greetMe()
        speak('Hello Sir, I am your digital assistant   swati   Lisa the Lady Jarvis!')
        speak('How may I help you?')

        while True:
            keyword=myCommand()
            keyword=keyword.lower()
            if 'jarvis' in keyword:
                playsound('C:/Users/USER/Downloads/Telegram Desktop/SVATI/when.mp3')
                msg=[' At your service sir!','Yes sir','How can i help you','Speak','I am listning','Yes']
                speak(random.choice(msg))

                main_process()
            else:
                continue

        


window.close()








