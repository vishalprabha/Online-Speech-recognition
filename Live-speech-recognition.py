#Live Speech recognition using Google api

import speech_recognition as sr

# use the audio file as the audio source
r = sr.Recognizer()

#use Microphone to record live Speech
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
    
#Read entire recorded audio source and send it through Google api
text = r.recognize_google(audio)
#Print the Translated text
print(text)
