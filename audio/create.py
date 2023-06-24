from gtts import gTTS
import os

def speak(sentence):
    tts = gTTS(sentence)
    tts.save("confusion.mp3")
    os.system("afplay output.mp3")


sentence = "Do I need to Google it or search it on Youtube"
speak(sentence)
