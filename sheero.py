import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import cv2
import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("I am sheero")
    speak("How can i help you?")

#voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query


if __name__ =="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if "open notepad" in query:
            npath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(npath)

        elif "open reader" in query:
            npath = "C:\\Program Files\\Adobe\\Acrobat DC\\Adobe Acrobat.exe "
            os.startfile(npath)


        elif "open command prompt" in query:
            os.system("start cmd")


        elif "images of csp" in query:
            npath = "C:\\Users\\SAI LOKESH\\Desktop\\ramya\\csp\\picsofcsp"
            os.startfile(npath)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
                if cv2.waitKey(1) & 0xff == ord(' '):  # By using space bar delay will stop
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music offline" in query:
            music_dir="F:\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "open google" in query:
            speak("what should i search in google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif "send message" in query:
            speak("what you want me to send?")
            cm=takecommand().lower()
            kit.sendwhatmsg_instantly("+919063901055",cm)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif "play songs on youtube" in query:
            speak("what you want me to play")
            cm=takecommand().lower()
            kit.playonyt(cm)

        elif "no" in query:
            speak("thank you for using me ")
            sys.exit()

        speak(" do you have any other work with me?")

















