import pywhatkit


class search():
    
    def srch(self, sentence: str):
        try:
            pywhatkit.search(sentence)
            print("Searching...")
        except:
            print("An unknown error occurred")
            raise

sr = search()