import speech_recognition as sr
from pytube import YouTube
from pathlib import Path

scribe = sr.Recognizer()

def Download(url):
    downloader = YouTube(url)
    downloader.streams.get_audio_only
    print("attempting.")
    try:
        downloader.download()
    except:
        print("Oh Sh#t")
    print("Download complete")
    
    
def Transcribe(file): 
    # https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py
    with sr.AudioFile(file) as source:
        audio = scribe.record(source)  # read the entire audio file
    try:
        print(scribe.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

if __name__ == "__main__":
    url = "https://youtu.be/amrCMakolKA" # What Is Irrigation?
    Download(url)
    #Transcribe(file)

