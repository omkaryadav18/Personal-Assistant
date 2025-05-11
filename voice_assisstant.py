import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

#initialize speech engine
engine = pyttsx3.init()

#func to asst speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Func to take a voice cmd from  user
def take_command():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Network Error.")
            return None
    
    return command.lower()

#Func to respond to diff cmds
def respond(command):
    if 'hello' in command or 'hi' in command:
        speak("Hello! How caan i asssist you today?")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif 'search' in command:
        speak(f"What would you like to search for?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https//www.google.com/search?q={search_query}")

    elif 'open' in command:
        if 'safari' in command:
            speak("Opening safari")
            os.system("open -a Safari")
        elif 'calculator' in command:
            speak("Opening calculator")
            os.system("open -a Calculator")

    elif 'bye' in command or 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("I'm sorry, i don't know that command.")

#Mainfunc to run ast
def run_asst():
    speak("Hello, I am your assistant. How can i help you?")
    while True:
        command = take_command()
        if command:
            respond(command)

#start asst
run_asst()