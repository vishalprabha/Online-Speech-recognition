# Speech recognition using recognize_google method present in Python speech_recognition library

import speech_recognition as sr

audio = 'Three.wav' # wav file name

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(audio) as source:
    audio = r.record(source) # read the entire audio file

# recognize speech using Google 
try:
    text = r.recognize_google(audio)
    print (text)

except Exception as e:
    print (e)
