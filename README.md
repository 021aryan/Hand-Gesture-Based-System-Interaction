
# Hand-Gesture Based System Interaction
Hand-gesture based system interaction refers to a method of controlling a digital system using hand movements and gestures, without the need for physical contact with input devices like a mouse or keyboard. The system uses a camera or sensor to capture the movements of the hand and interprets them as commands. This technology is commonly used in virtual reality, gaming, and smart homes.





# Libraries Used
- pyttsx3==2.71: pyttsx3 is a text-to-speech conversion library in Python.Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
- SpeechRecognition==3.8.1: Library for performing speech recognition, with support for several engines and APIs, online and offline.
- pynput==1.7.3: This library allows you to control and monitor input devices. Currently, mouse and keyboard input and monitoring are supported.
- pyautogui==0.9.53: PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard. pip install pyautogui.
- wikipedia==1.4.0: The Wikipedia Library is an open research hub, a place for active Wikipedia editors to gain access to the vital reliable sources that they need to do their work and to be supported in using those resources to improve the encyclopedia.
- opencv-python==4.5.3.56: Python bindings for OpenCV are developed in official OpenCV repository and it's the best place to report issues.
- mediapipe==0.8.6.2: MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web.
- comtypes==1.1.11: comtypes is a lightweight Python COM package, based on the ctypes FFI library, in less than 10000 lines of code (not counting the tests).
- pycaw==20181226: Pycaw is a Python library that provide
- screen-brightness-control==0.9.0:  A Python tool for controlling the brightness of your monitor. Supports Windows and most flavours of Linux.
- eel==0.14.0: Eel is a little Python library for making simple Electron-like offline HTML/JS GUI apps, with full access to Python capabilities and libraries.
# Procedure
- Gesture recognition: This component would be responsible for recognizing the gestures made by the user and translating them into commands for the system. This could involve the use of cameras, sensors, or other technologies that can detect and interpret physical movements.
- User interface: The user interface would be the visual component of the system that displays information to the user and allows them to interact with the system using gestures.
- Gesture library: The gesture library would be a database of predefined gestures that the system recognizes and associates with specific actions or commands. Users could learn these gestures and use them to interact with the system in a consistent and intuitive way.
- Training and customization: The system could include features that allow users to train the system to recognize new gestures or customize existing gestures to better fit their needs or preferences.
- Integration with other systems: The gesture-based system interaction could be integrated with other systems, such as smart home devices or virtual assistants, to provide a seamless and intuitive user experience across multiple devices and platforms.
- User Manual: To use a hand gesture definition, you must first learn the gestures and understand what actions they are associated with. The user manual is presented to provide an understanding of the gestures needed to be performed in certain order to achieve the required outcomes.
- Third party software: We have made use of Yawcam software. Yawcam - Yet Another Webcam Software, The main ideas for Yawcam are to keep it simple and easy to use but to include all the usual features.




# Requirements 
## Functional Requirements
- Image processing: It’s used to identify object type & It’s a method in which a user’s  image will be detected. also, by the help of these, you can calculate height. 
- Video Processing: In that real-time Analysis will be done in the human body will be    detected. With the help of these, we have detected human body postures while workout. In that n number of images will be processed. 
- Open CV Library : Open CV it's an open-source package or a library which is aimed   at real-time computer vision & ML it's a cross-platform which can support various languages. Open CV is one of the most widely used applications of computer vision gesture recognition motion understanding object detection, segmentation, and recognition. 

## Non-Functional Requirements
- The program must be self-contained so that it can easily be moved from one Computer to another.
- It is assumed that network connection will be available on the computer on which the program  resides.
- Interoperability and availability.
	The system shall achieve 100 per cent availability at all times.
- Maintainability
			The system should be optimized for supportability, or ease of maintenance as far as 				possible. This may be achieved through the use documentation of coding standards, naming 			conventions, class libraries and abstraction.
- Reliability

## Hardware Requirements
- System: Intel i5
- Hard Disk: 120 GB
- Monitor: 15"LED
- Input Devices: Keyboard, Mouse, Camera 
- Ram: 4 GB

## Software Requirements
- Operating system: Windows 10 64-bit  
- Coding Language: PYTHON 3.8.5 
- Tools: Anaconda Navigator



### Procedure

  Step 1: 
  ```bash
  conda create --name gest python=3.8.5
  ```
  
  Step 2:
  ```bash
  conda activate gest
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  conda install PyAudio
  ```
  ```bash 
  conda install pywin32
  ```
  
  Step 5:
  ``` 
  cd to the GitHub Repo till src folder
  ```
  Command may look like: `cd C:\Users\.....\Gesture-Controlled-Virtual-Mouse\src`
  
  Step 6:
  
  For running Voice Assistant:
  ```bash 
  python Proton.py
  ```
  ( You can enable Gesture Recognition by using the command "Proton Launch Gesture Recognition" )
  
  Or to run only Gesture Recognition without the voice assisstant:
  
  Uncomment last 2 lines of Code in the file `Gesture_Controller.py`
  ```bash 
  python Gesture_Controller.py
  ```


    
## Screenshots
![Picture1](https://github.com/021aryan/Hand-Gesture-Based-System-Interaction/assets/91712563/78155a84-ce87-4343-986e-4c0ad0defd85)
![Picture2](https://github.com/021aryan/Hand-Gesture-Based-System-Interaction/assets/91712563/b6f2631f-a9e2-43c4-a0e9-e4faae9ff4b0)
![Picture3](https://github.com/021aryan/Hand-Gesture-Based-System-Interaction/assets/91712563/030e7e22-1643-43ec-a085-49ad459636a5)
![Picture4](https://github.com/021aryan/Hand-Gesture-Based-System-Interaction/assets/91712563/4118033e-a492-44df-a0bb-81a997fde767)
