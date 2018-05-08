import wave
import pyaudio
import speech_recognition as sr

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 3


def recordAudio(filename):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def recordData():

    filename = "test.wav"
    recordAudio(filename)
    googlecall(filename)

def googlecall(filename):
    audio = filename # wav file name

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

recordData()
