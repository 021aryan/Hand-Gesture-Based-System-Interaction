import pyttsx3
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import cv2
import mediapipe as mp
import datetime
import threading
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
import Gesture_Controller
from skimage.metrics import structural_similarity as ssim
import User_Manual
from User_Manual import run_gui
#import Gesture_Controller_Gloved as Gesture_Controller
import app
from threading import Thread


# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



# ----------------Variables------------------------
file_exp_status = False
files =[]
path = ''
is_awake = True  #Bot status

# ------------------Functions----------------------
def reply(audio):
    app.ChatBot.addAppMsg(audio)

    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        reply("Good Morning!")
    elif hour>=12 and hour<18:
        reply("Good Afternoon!")   
    else:
        reply("Good Evening!")  
        
    reply("I am Nova, how may I help you?")

# Set Microphone parameters
with sr.Microphone() as source:
        r.energy_threshold = 500 
        r.dynamic_energy_threshold = False

# Audio to String
def record_audio():
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError:
            print('cant recognize')
            pass
        return voice_data.lower()

def start_gui():
    gui_thread = threading.Thread(target=User_Manual.run_gui_thread)
    gui_thread.start()
# Executes Commands (input: string)
def respond(voice_data):
    lgr=['launch gesture recognition','launch just a recognition','start just a recognition','start gesture recognition', 'run just a recognition','run gesture recognition']
    sgr=['stop gesture recognition','top gesture recognition','stock gesture recognition','stop just a recognition','top just a recognition','stock just a recognition']
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('nova','')
    app.eel.addUserMsg(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    # STATIC CONTROLS
    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply('My name is Nova!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif 'search' in voice_data:
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found')
        except:
            reply('Please check your Internet')

    elif 'location' in voice_data:
        reply('Which place are you looking for ?')
        temp_audio = record_audio()
        app.eel.addUserMsg(temp_audio)
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found')
        except:
            reply('Please check your Internet')

    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Good bye Sir! Have a nice day.")
        is_awake = False

    elif ('exit' in voice_data) or ('terminate' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
        app.ChatBot.close()
        #sys.exit() always raises SystemExit, Handle it in main loop
        sys.exit()
        
    
    # DYNAMIC CONTROLS
    elif ('launch gesture recognition' in voice_data) or ('launch just a recognition' in voice_data) or ('start just a recognition' in voice_data) or ('start gesture recognition' in voice_data) or ('run just a recognition' in voice_data) or ('run gesture recognition' in voice_data) or ('launch justice recognition' in voice_data) :
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active')
        else:
            gc = Gesture_Controller.GestureController()
            t = Thread(target = gc.start)
            t.start()
            start_gui()
            reply('Launched Successfully')

    elif ('stop gesture recognition' in voice_data) or ('top gesture recognition' in voice_data) or ('stock gesture recognition' in voice_data) or ('stop just a recognition' in voice_data) or ('top just a recognition' in voice_data) or ('stock just a recognition' in voice_data) or ('stock justice recognition' in voice_data) :
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped')
        else:
            reply('Gesture recognition is already inactive')
        
    
                   
    else: 
        reply('I am not functioned to do this!')

# ------------------Driver Code--------------------
image_paths = ["felix.png","abc.jpg", "kaushik.jpg"]
images = [cv2.imread(path) for path in image_paths]
match= False

mp_face_detection = mp.solutions.face_detection.FaceDetection()

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video capture
    ret, frame = cap.read()
    
    # Detect faces in the frame
    results = mp_face_detection.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Check if a face was detected
    if results.detections:
        # Extract face ROI
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            h, w, _ = frame.shape
            face_roi = frame[int(bbox.ymin * h):int((bbox.ymin + bbox.height) * h), 
                              int(bbox.xmin * w):int((bbox.xmin + bbox.width) * w)]
            
        
        # Resize face ROI and image
        face_roi = cv2.resize(face_roi, (720, 720))
        for image in images:

            image = cv2.resize(image, (720, 720))
        
            # Compare images using SSIM
            similarity = ssim(cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY),
                              cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        
            if similarity > 0.49:
                print("Face Matched.")
                match= True
                t1 = Thread(target = app.ChatBot.start)
                t1.start()
                break
        if match:
            break
            

    # Display the resulting frame
    cv2.imshow('Face Recognition',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') & match:
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()




# Lock main thread until Chatbot has started
while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:
    if app.ChatBot.isUserInput():
        #take input from GUI
        voice_data = app.ChatBot.popUserInput()
    else:
        #take input from Voice
        voice_data = record_audio()

    #process voice_data
    if 'nova' in voice_data:
        try:
            #Handle sys.exit()
            respond(voice_data)
        except SystemExit:
            reply("Exit Successfull")
            break
        except:
            #some other exception got raised
            print("EXCEPTION raised while closing.") 
            break
        


