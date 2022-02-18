import random
from puzzle_2 import main_2
import sys
from match import Puzzle

class Player:

    def __init__(self):
        self._puzzle = Puzzle()
        self._guess = ""
        self._guesses = []
        self._incorrect_guess = []
        self._guesses_left = 20
        self._guesses_allowed = 20
    def guess_word(self):
        print("The number of letters are: ", len(self._puzzle._word))
        print("The first letter is: ", self._puzzle._word[0], "\nAnd the last one is: ",self._puzzle._word[-1])
        self._guess = input("\nEnter a letter: ")
        self._guesses.append(self._guess)
    def check_guess(self):
        if self._guess in self._puzzle._word:
            self.warning()
            print("Correct!")
        else:
            print("Incorrect!")
            self.warning()
            self._incorrect_guess.append(self._guess)
            poping = self._guesses.pop()
            self._guesses_left -= 1
    def display_incorrect(self):
        print("Letters you guesses that were wrong! ", self._incorrect_guess)
    def display_word(self):
        print("The word is: ", self._puzzle._word)
    def display_guesses(self):
        print("Lines in your parachute: ", self._guesses)
    def display_guesses_left(self):
        print("Lines in your parachute left: ", self._guesses_left)
    def warning(self):
        print("DO NOT UNDER ANY CIRCUMSTANCES USE THE SAME LETTER MORE THAN ONCE")
    def play_game(self):

        while self._guesses_left > 0:
            self.guess_word()
            self.check_guess()
            self.display_guesses()
            self.display_guesses_left()
            self.display_incorrect()
            
            if self._guesses_left == 0:
                print("\nYou lost!") 
                print("I'm so sorry, but you lost the game. Be thankful that this is just a game, otherwise you could have lost your life :( ")
                print(self.display_word())
                
                restart = input("Do want to play Again?(y/n): ")
                if restart.lower() == "y":
                    main()
                else:
                    sys.exit
            new_trans = ''.join(map(str, self._guesses))
            if new_trans == self._puzzle._word:
                print("You won!! Congrats!!")
                print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                restart = input("Do want to play Again?(y/n): ")
                if restart.lower() == "y":
                    main()
                else:
                    sys.exit
            else:
                #Let's check if the player has guessed the word. This will only be used if the player does not guess the word
                #in its correct order
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
                    case 5:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 6:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 7:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 8:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 9:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 10:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 11:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 12:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 13:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 14:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 15:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses and self._puzzle._word[14] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break
                    case 16:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses and self._puzzle._word[14] in self._guesses and self._puzzle._word[15] in self._guesses:
                            print("\nWell done! you finally made it!!")
                            print("To celebrate your victory I would invite you a beer but my creator does not drink beer, I am a computer program and I guess you don't drink beer either. So I will just say, well done!")
                            print("The word was",  self._puzzle._word)
                            break


def main():
    obj1 = Puzzle()
    player = Player()
    player.play_game()

print("Welcome to the word game!")
print("\nThere are multiple rooms, which one do you want to go to?(1/2) ")
print("Just remember, room 1 has thousands of words, room 2 has only ten words.")
choice = input("\nEnter 1 or 2: ")

if choice == "1":
    print("\nYou are in room 1")
    print("You have three thousand words to guess.")
    print("You have 20 lines in your parachute.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main()

elif choice == "2":
    print("\nYou are in room 2")
    print("You have ten words to guess.")
    print("You have 10 lines in your parachute.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main_2()
