import pyttsx3
import speech_recognition as sr
import pyautogui as p
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    # engine.say(audio)
    print(audio)   
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # speak("Speak Now")
        r.pause_threshold = 1
        while True:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-US')
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio. Retrying...")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                break  # Exit the loop if a request error occurs


def process_command(command):
    if command == "exit":  # Check if command is "exit"
        exit(0)
    if "play" in command or "start" in command or "pause" in command or "stop" in command:
        p.press("space")
    elif "volume plus" in command or "volume up" in command:
        for _ in range(5):  # Press "up" key 5 times
            p.press("up")
    elif "volume minus" in command or "volume down" in command:
        for _ in range(5):  # Press "down" key 5 times
            p.press("down")
    elif "forward" in command:
        p.keyDown("ctrl")
        p.press("right")
        p.keyUp("ctrl")
    elif "backward" in command:
        p.keyDown("ctrl")
        p.press("left")
        p.keyUp("ctrl")


def main():
    while True:
        command = take_command()
        if command:
            process_command(command)


if __name__ == "__main__":
    main()
