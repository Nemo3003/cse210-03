import random
from re import match
import sys
from match import Words

class Parachuter:
    def __init__(self):
        self._puzzle = Words()
        self._guess = ""
        self._guesses = []
        self._incorrect_guess = []
        self._guesses_left = 10
        self._guesses_allowed = 10
    
    def guess_word(self):
        length_word =  len(self._puzzle._word)
        print("The number of letters are: ", length_word)
        print("The first letter is: ", self._puzzle._word[0])
        self._guess = input("\nEnter a letter: ")
        self._guesses.append(self._guess)
    def check_guess(self):
        if self._guess in self._puzzle._word:
            self.warning()
            print("\nCorrect!")
        else:
            print("\nIncorrect!")
            self.warning()
            self._incorrect_guess.append(self._guess)
            poping = self._guesses.pop()
            self._guesses_left -= 1
    def display_incorrect(self):
        print("Letters you guesses that were wrong! ", self._incorrect_guess)
    def display_guesses(self):
        print("Your guesses: ", self._guesses)
    def display_guesses_left(self):
        print("Guesses left: ", self._guesses_left)
    def warning(self):
        print("DO NOT UNDER ANY CIRCUMSTANCES USE THE SAME LETTER MORE THAN ONCE")
    def play_game(self):
        list_new = self._guesses

        while self._guesses_left > 0:
            self.guess_word()
            self.check_guess()
            self.display_guesses()
            self.display_guesses_left()
            self.display_incorrect()
            
            if self._guesses_left == 0:
                print("\nYou lost!")
                print("I'm so sorry, but you lost the game. Be thankful that this is just a game, otherwise you could have lost your life :( ")
                restart = input("Do want to play Again?(y/n): ")
                if restart.lower() == "y":
                    main_2()
                else:
                    sys.exit
            
            new_trans = ''.join(map(str, self._guesses))
            if new_trans == self._puzzle._word:
                print("You won!! Congrats!!")
                print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                restart = input("Do want to play Again?(y/n): ")
                if restart.lower() == "y":
                    main_2()
                else:
                    sys.exit
            else:
                length_word =  len(self._puzzle._word)
                match length_word:
                    case 2:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 3:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 4:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break

def main_2 ():
    obj1 = Parachuter()
    obj1.play_game()
