import pywhatkit
import re

class ycls():
    sentence = ""

    @staticmethod
    def extract_substring(text):
        start_match = re.search(r'\bplay\b', text)
        if start_match:
            start = start_match.end()
        else:
            return ""

        # Extract the substring
        substring = text[start:].strip()

        return substring

    def get_string(self, sentence:str):
        self.sentence = sentence
        try:
            pywhatkit.playonyt(self.extract_substring(sentence.lower()))
            print("Playing...")
        except:
            print("Network Error Occurred")
            raise
    
yt = ycls()