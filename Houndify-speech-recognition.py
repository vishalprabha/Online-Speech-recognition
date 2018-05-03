# Code Taken from Python Speech Recognition
# You can get your Houndify Keys by creating an account in their website
# This doesn't recognize accurately for Indian accent 

import speech_recognition as sr

# obtain path to "Three.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "Three.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "Enter your client_id"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "Enter your client_key"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
