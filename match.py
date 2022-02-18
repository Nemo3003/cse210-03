import random

class Word:
    def __init__(self):
        fileObject = open("list_words.txt", "r")
        data = fileObject.read()
        self.longest_string = max(data, key=len)
        self._word = random.choice(data.split())
class Puzzle(Word):
    def __init__(self):

        # Calling constructor of the word class
        Word.__init__(self)


#-----------------------------------------------------------------------------------------------------------------------
#Shorter list

class Words:
    def __init__(self):
        self.data = ["be", "have", "do", "say","get","make", "go", "know", "take","see"]
        self._word = random.choice(self.data)
    def get_word(self):
        return self._word
class Puzzles(Words):
    def __init__(self):

        # Calling constructor of the word class
     Words.__init__(self)