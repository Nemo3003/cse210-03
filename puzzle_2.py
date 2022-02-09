import random

class Words:
    def __init__(self):
        self.data = ["be", "have", "do", "say","get","make", "go", "know", "take","see"]
        self._word = random.choice(self.data)
    def get_word(self):
        return self._word
class Puzzle(Words):
    def __init__(self):

        # Calling constructor of the word class
     Words.__init__(self)
class Parachuter:
    def __init__(self):
        self._puzzle = Words()
        self._guess = ""
        self._guesses = []
        self._guesses_left = 10
        self._guesses_allowed = 10
    def guess_word(self):
        print("The number of letters are: ", len(self._puzzle._word))
        print("The first letter is: ", self._puzzle._word[0])
        self._guess = input("\nEnter a letter: ")
        self._guesses.append(self._guess)
    def check_guess(self):

        if self._guess in self._puzzle._word:
            print("\nCorrect!")
        else:
            print("\nIncorrect!")
            poping = self._guesses.pop()
            self._guesses_left -= 1
    def display_word(self):
        print("The word is: ", self._puzzle._word)
    def display_guesses(self):
        print("Your guesses: ", self._guesses)
    def display_guesses_left(self):
        print("Guesses left: ", self._guesses_left)

    def play_game(self):
        list_new = self._guesses

        while self._guesses_left > 0:
            self.guess_word()
            self.check_guess()
            self.display_guesses()
            self.display_guesses_left()
            self.display_word()
            if self._guesses_left == 0:
                print("\nYou lost!")
                print(self.display_word())
                break

            new_trans = ''.join(map(str, self._guesses))
            if new_trans == self._puzzle._word:
                print("You won!! Congrats!!")
                print(self.display_word())
                break

def main_2 ():
    obj1 = Parachuter()
    obj1.play_game()