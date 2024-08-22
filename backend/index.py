import json
import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
from flask import Flask # type: ignore


recognizer = sr.Recognizer()
engine = pyttsx3.init()
app = Flask(__name__)

answers = "data.json"
with open(answers, "r") as file:
    data = json.load(file)


#def google_search(query):
def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio from the microphone and return the recognized text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, the service is down.")
            return ""

def handle_query(query):
    """Process the recognized speech and respond"""
    questions=[
        "hello",
        "what is your name",
        "how are you",
        "exit",
        "quit",
        "what can you do",
        "what is Gino's digital",
        "who is Gilbert"
    ]
    if " " in query:
        mod = query.replace(" ", "-")
        speak(data[mod])
        
    elif " " not in query:
        if query == 'exit' or query == 'quit':
            speak(data[query])
            exit(0)
        else:
            speak(data[query])
            
    else:
        speak("I could not hear you there. Can you try again?")
    

@app.route('/')
def index():
    return "hitting 5000 from docker"

def activate_helper():
    while True:
        query = listen()
        if query:
            handle_query(query)


@app.route('/activate', methods=['GET'])
def activate_voice_assistant():
    activate_helper()



if __name__ == "__main__":
    activate_helper()
    app.run(host='0.0.0.0', port=5000)
    

    
    
    
    