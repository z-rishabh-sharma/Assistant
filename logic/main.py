from services.youtube import yt
from services.search import sr
from playsound import playsound


class M():
    stop = False
    astring = False
    pause = False
    local_string = []
    list_question = ["search", "what", "which", "when", "where", "who", "whom", "whose", "why", "whether", "how", "google"]

    def logic(self, sentence: str) -> None:
        
        search_flag = False
        if self.astring:
            self.stop = True

        for word in self.list_question:
            if word in sentence:
                search_flag = True
                

        if 'play' in sentence.lower() and self.pause == False:
            if self.astring:
                yt.get_string(sentence=self.local_string[0].lower()) # Work fine
                self.astring = False
            else:
                yt.get_string(sentence=sentence.lower())
            self.stop = False
            
        elif search_flag and self.pause == False:
            if self.astring:
                sr.srch(sentence=self.local_string[0].lower())
                self.astring = False
            else:
                sr.srch(sentence=sentence.lower()) # Work fine
            self.stop = False
        elif "stop" in sentence:
            self.pause = True
        elif "start" in sentence:
            self.pause = False
        else:
            if self.pause == False:
                self.stop = True
                self.local_string.append(sentence)
                playsound('audio/confusion.mp3')
                self.astring = True
                self.stop = False

m = M()