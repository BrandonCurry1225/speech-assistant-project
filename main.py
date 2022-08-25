from gtts import gTTS
import playsound
import speech_recognition as sr
import webbrowser
import os
import random
from time import ctime
import time

# Set voice recognizer
r = sr.Recognizer()

def record_audio(ask = False):

    # To set input audio as microphone
    with sr.Microphone() as source:

        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak('sorry, I did not get that. Please try again.\n')
        except sr.RequestError:
            alexa_speak('sorry, my speech service is down\n')
        return voice_data

# For creating voice
def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = os.path.dirname(__file__) + 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# For main choices
def respond(voice_data):

    if 'what is your name' in voice_data:
        alexa_speak('My name is whatever you wish to call me by.\n')

    if 'what time is it' in voice_data:
        alexa_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='\
              + search
        webbrowser.get().open(url)
        alexa_speak('Here is what I found for ' + search)

    if 'location' in voice_data:
        location = record_audio('What is the location you are looking for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Here is the location of ' + location)

    if 'youtube' in voice_data:
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        alexa_speak('Here is youtube.')

    if 'amazon' in voice_data:
        url = 'https://www.amazon.com/'
        webbrowser.get().open(url)
        alexa_speak('Here is amazon.')

    if 'disney plus' in voice_data:
        url = 'https://www.disneyplus.com/home'
        webbrowser.get().open(url)
        alexa_speak("Here is Disney+.")

    if 'music' in voice_data:
        print("VOICE COMMANDS:\n" 
              "1. jazz\n"
              "2. rock\n"
              "3. country\n")
        voice_music = record_audio("What kind of music are you in the mood for?")
        play_music(voice_music)

    if 'tell a joke' in voice_data:
        alexa_speak('Why did the chicken cross the road? To get to the other side.')

    if 'make a note' in voice_data:
        notes = ['']
        item = record_audio("Say a note for me to remember.")
        notes.append(item)
        alexa_speak('This is your current note:')
        for item in notes:
            alexa_speak(str(item))

    if 'exit' in voice_data:
        exit()

def play_music(voice_music):

    if 'jazz' in voice_music:
        url = 'https://www.youtube.com/watch?v=neV3EPgvZ3g&t=6s'
        webbrowser.get().open(url)
        alexa_speak('Here is your jazz music')

    if 'rock' in voice_music:
        url = 'https://www.youtube.com/watch?v=YJlsJDE4bqM'
        webbrowser.get().open(url)
        alexa_speak('Here is your rock music')

    if 'country' in voice_music:
        url = 'https://www.youtube.com/watch?v=EqhsvSCW4uI'
        webbrowser.get().open(url)
        alexa_speak('Here is your country music')

# For beginning dialogue
print("\n")
print("Launching virtual assistant...\n")
print("VOICE COMMANDS:\n"
      "1. What is your name?\n"
      "2. What time is it?\n"
      "3. Search (google)\n"
      "4. Location (google maps)\n"
      "5. Youtube\n"
      "6. Amazon\n"
      "7. Disney+\n"
      "8. Music\n"
      "9. Tell a joke\n"
      "10. Make a note\n"
      "11. Exit (program)\n")
time.sleep(1)
alexa_speak('Hello, how can I help you?\n')
while 1:
    voice_data = record_audio()
    respond(voice_data)
