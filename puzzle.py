import random
from puzzle_2 import main_2
#TODO: Add a check to see if the player got the word right

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

class Player:

    def __init__(self):
        self._puzzle = Puzzle()
        self._guess = ""
        self._guesses = []
        self._guesses_left = 20
        self._guesses_allowed = 20
    def guess_word(self):
        print("The number of letters are: ", len(self._puzzle._word))
        print("The first letter is: ", self._puzzle._word[0], "\nAnd the last one is: ",self._puzzle._word[-1])
        self._guess = input("\nEnter a letter: ")
        self._guesses.append(self._guess)
    def check_guess(self):
        if self._guess in self._puzzle._word:
            print("Correct!")
        else:
            print("Incorrect!")
            poping = self._guesses.pop()
            self._guesses_left -= 1
    def display_word(self):
        print("The word is: ", self._puzzle._word)
    def display_guesses(self):
        print("Lines in your parachute: ", self._guesses)
    def display_guesses_left(self):
        print("Lines in your parachute left: ", self._guesses_left)

    def play_game(self):

        while self._guesses_left > 0:
            self.guess_word()
            self.check_guess()
            self.display_guesses()
            self.display_guesses_left()
            if self._guesses_left == 0:
                print("\nYou lost!")
                print(self.display_word())
                break
            new_trans = ''.join(map(str, self._guesses))
            if new_trans == self._puzzle._word:
                print("You won!! Congrats!!")
                break
            else:
                length_word =  len(self._puzzle._word)
                match length_word:
                    case 2:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 3:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 4:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 5:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 6:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 7:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 8:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 9:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 10:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 11:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 12:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 13:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 14:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 15:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses and self._puzzle._word[14] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)
                    case 16:
                        if self._puzzle._word[0] in self._guesses and self._puzzle._word[1] in self._guesses and self._puzzle._word[2] in self._guesses and self._puzzle._word[3] in self._guesses and self._puzzle._word[4] in self._guesses and self._puzzle._word[5] in self._guesses and self._puzzle._word[6] in self._guesses and self._puzzle._word[7] in self._guesses and self._puzzle._word[8] in self._guesses and self._puzzle._word[9] in self._guesses and self._puzzle._word[10] in self._guesses and self._puzzle._word[11] in self._guesses and self._puzzle._word[12] in self._guesses and self._puzzle._word[13] in self._guesses and self._puzzle._word[14] in self._guesses and self._puzzle._word[15] in self._guesses:
                            print("Well done! you finally made it!!")
                            print("The word was",  self._puzzle._word)


def main():
    obj1 = Puzzle()
    player = Player()
    player.play_game()

print("Welcome to the word game!")
print("\nThere are multiple rooms, which one do you want to go to?(1/2) ")
print("Just remember, room 1 has thousands of words, room 2 has only ten words.")
choice = input("\nEnter 1 or 2: ")

if choice == "1":
    print("You are in room 1")
    print("You have three thousand words to guess.")
    print("You have 20 lines in your parachute.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main()

elif choice == "2":
    print("You are in room 2")
    print("You have ten words to guess.")
    print("You have 10 lines in your parachute.")
    print("You can only guess one letter at a time.")
    print("Good luck!")
    main_2()
