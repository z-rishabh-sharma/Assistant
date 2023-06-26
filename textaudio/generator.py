import os
from gtts import gTTS

class convert():
    val = 1
    def speak(self, sentence):
        tts = gTTS(sentence)
        tts.save(f"list_{self.val}.mp3")
        self.val += 1



dir_path = os.path.dirname(os.path.realpath(__file__))
list_file = []


for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            list_file.append(file)

size = len(list_file)
s = ", ".join(list_file)

result_1 = f'{size} records are found. Do you like if I tell you all.'
result_2 = f'Okay So the records are {s}'


sp = convert()