import speech_recognition as sr
from logic.main import m

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        microphone = sr.Microphone()
        print("Listening...")

        with microphone as source:
            audio = self.recognizer.listen(source, phrase_time_limit=5)  # Set a time limit of 5 seconds for speech recognition

        try:
            if(m.stop == False):
                sentence = self.recognizer.recognize_google(audio)
                print("You said:", sentence)
                return sentence.lower()
        except sr.UnknownValueError:
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            print("Error occurred:", str(e))

        return None


if __name__ == "__main__":
    speech_to_text = SpeechToText()

    while True:
        sentence = speech_to_text.listen()

        if sentence is not None:
            if "quit" in sentence:
                print("Terminating the code...")
                break
            else:
                print("Processing the sentence:", sentence)
                m.logic(sentence)
        else:
            print("No speech detected.")

    print("Code terminated.")
