
import gtts as gt
import os
import pyttsx3
from playsound import playsound
import speech_recognition as sr
from datetime import datetime
from translate import Translator
import webbrowser
from bs4 import BeautifulSoup
import requests

## USER-SPEECH TO TEXT (USER) TAMIL

def tamilSpeechToText():
    text = ""
    global WhatUSpoke
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something in Tamil")
        playsound("beep.mp3")
        audio = r.listen(source)
        playsound("pika.mp3")
        try:
            # language="ta-IN"
            text = r.recognize_google(audio, language="ta-IN")
            print("What you spoke :", text)

        except Exception:
            print("recognition failed")

        return text


### TEXT TO SPEECH (MACHINE) TAMIL

def tamilTextToSpeech(speak):
    # TamilText = "சம் சூப்பர் ஹீரோ சூப்பர் ஹீரோ!"
    tts = gt.gTTS(text=speak, lang='ta')
    tts.save("Tamil-Audio.mp3")
    # os.system("Tamil-Audio.mp3")
    playsound("Tamil-Audio.mp3")

# TEXT TO SPEECH

def Speak(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    # Use female voice
    engine.setProperty('voice', voice_id)
    engine.runAndWait()


### CONTENT FOR SPEAKING

now = datetime.now()
output = tamilSpeechToText()

if "உன் பெயர் என்ன" in output:
    tamilTextToSpeech("என் பெயர் நிலா")
    print("என் பெயர் நிலா")
elif "ஹாய்" in output:
    tamilTextToSpeech("வணக்கம், நீ் எப்டி இருக்க")
    print("வணக்கம், நீ் எப்டி இருக்க")
elif "வணக்கம்" in output:
    tamilTextToSpeech("வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்")
    print("வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்")
elif "நாள்" in output:
    today = datetime.today()
    current_day = today.strftime("%A")
    translation = Translator.translate(current_day)
    tamilTextToSpeech("இன்று" + translation + "கிழமை")
    print("இன்று", translation, "கிழமை")

else:
    tamilTextToSpeech(output)
