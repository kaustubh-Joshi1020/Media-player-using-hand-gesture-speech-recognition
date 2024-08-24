from django.shortcuts import render

import cv2
import mediapipe as mp
import pyautogui
import time

import pyttsx3
import speech_recognition as sr
import pyautogui as p
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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
                break


def process_command(command):
    if command == "exit":
        exit(0)
    if "play" in command or "start" in command or "pause" in command or "stop" in command:
        p.press("space")
        print("Media playback command recognized")
    elif "volume plus" in command or "volume up" in command:
        for _ in range(5):
            p.press("up")
        print("Volume increased")
    elif "volume minus" in command or "volume down" in command:
        for _ in range(5):
            p.press("down")
        print("Volume decreased")
    elif "next" in command:
        p.press("right")
        print("next command recognized")
    elif "previous" in command:
        p.press("left")
        print("previous command recognized")
    elif "forward" in command:
        p.press("w")
        print("Forward command recognized")
    elif "backward" in command:
        p.press("q")
        print("Backward command recognized")


def handle_speech_recognition():
    while True:
        try:
            command = take_command()
            if command:
                process_command(command)
        except Exception as e:
            print(f"An error occurred in speech recognition: {e}")


def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt


def handle_hand_gesture():
    cap = cv2.VideoCapture(0)
    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=1)

    start_init = False
    prev = -1

    while True:
        try:
            end_time = time.time()
            _, frm = cap.read()
            frm = cv2.flip(frm, 1)

            res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

            if res.multi_hand_landmarks:
                hand_keyPoints = res.multi_hand_landmarks[0]
                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):
                            pyautogui.press("right")
                            print("Right gesture detected")
                        elif (cnt == 2):
                            pyautogui.press("left")
                            print("Left gesture detected")
                        elif (cnt == 3):
                            pyautogui.press("up")
                            print("Up gesture detected")
                        elif (cnt == 4):
                            pyautogui.press("down")
                            print("Down gesture detected")
                        elif (cnt == 5):
                            pyautogui.press("space")
                            print("Space gesture detected")
                        prev = cnt
                        start_init = False

                drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

            cv2.imshow("window", frm)
            key = cv2.waitKeyEx(1)
            if key == 27:
                cv2.destroyAllWindows()
                cap.release()
                break
        except Exception as e:
            print(f"An error occurred in hand gesture recognition: {e}")
            cv2.destroyAllWindows()
            cap.release()


def main():
    speech_thread = threading.Thread(target=handle_speech_recognition)
    gesture_thread = threading.Thread(target=handle_hand_gesture)

    speech_thread.start()
    gesture_thread.start()


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("Terminated by user")


# Create your views here.
def index(request):
    try:
        main()
    except KeyboardInterrupt:
        print("Terminated by user")
    return render(request , "homepage.html")

def video(request):
    return render(request , "video.html")

def music(request):
    return render(request , "music.html")
