import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice for the assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Change index to select a different voice

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("You said: ", text)
            return text.lower()
        except:
            print("Sorry, I could not understand. Please try again.")
            return ""

# Function to process user input and respond
def process_input(input):
    if "hello" in input:
        speak("Hello, how can I assist you?")
    elif "what's the weather like today" in input:
        speak("I am sorry, I cannot provide that information at the moment.")
    elif "goodbye" in input:
        speak("Goodbye, have a nice day!")
        exit()
    else:
        speak("I am sorry, I did not understand what you said. Can you please repeat?")

# Main loop to listen for user input and respond
while True:
    input = listen()
    process_input(input)
