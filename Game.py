import copy

from Data import *


class Game:

    def __init__(self):
        self.__score = 0
        self.__is_running = True
        self.__game_order = generate_new_order()
        self.__clue_one = self.__get_next_value()
        self.__clue_two = self.__get_next_value()

    def play(self):
        print("-" * 13)
        print("| NEW GAME: |")
        print("-" * 13)
        self.play_round()

    def play_round(self):
        print("-" * (12 + len(str(self.__score + 1))))
        print("| ROUND: " + str(self.__score + 1) + " |")
        print("-" * (12 + len(str(self.__score + 1))))
        # display clues:
        print(self.__clue_one["name"] + " with a time of: " + str(self.__clue_one["time"])
              + " is higher or lower than: " + self.__clue_two["name"] + "?")

        # wait for input
        var = input("h/l:")

        # verify input type:
        if var[0] == "h":
            guess_higher = True
        elif var[0] == "l":
            guess_higher = False
        else:
            print("unrecognized guess, try again")
            return self.play_round()

        # process whether guess was correct
        if guess_higher and self.__clue_one["time"] >= self.__clue_two["time"]:
            self.correct_guess("higher")
        elif not guess_higher and self.__clue_one["time"] <= self.__clue_two["time"]:
            self.correct_guess("lower")
        elif guess_higher:
            self.incorrect_guess("higher")
        elif not guess_higher:
            self.incorrect_guess("lower")

    # pops the top element on the list
    def __get_next_value(self):
        if len(self.__game_order) == 0:
            self.game_won()
            return
        return self.__game_order.pop()

    # if the guess was correct, update the clues and play another round
    def correct_guess(self, guess_type):
        print("correct! " + self.__clue_one["name"] + " (" + str(self.__clue_one["time"]) + ")"
              + " has a " + guess_type + " time than "
              + self.__clue_two["name"] + " (" + str(self.__clue_two["time"]) + ")")
        self.__score = self.__score + 1
        self.__clue_one = self.__clue_two
        self.__clue_two = self.__get_next_value()
        if self.__is_running:
            self.play_round()

    # if incorrect guess, end the game
    def incorrect_guess(self, guess_type):
        print("incorrect! " + self.__clue_one["name"] + " (" + str(self.__clue_one["time"]) + ")" + " does not have a "
              + guess_type + " time than "
              + self.__clue_two["name"] + " (" + str(self.__clue_two["time"]) + ")")
        self.game_lost()

    # if somehow they win the game
    def game_won(self):
        print("Congrats! You win 0.o")
        self.__is_running = False

    # lost game
    def game_lost(self):
        print("You Lost!")
        print("score: " + str(self.__score))
        self.__is_running = False

    # getters
    def get_is_running(self):
        return self.__is_running

    def get_clue_one(self):
        return copy.copy(self.__clue_one)

    def get_clue_two(self):
        return copy.copy(self.__clue_two)

    def get_score(self):
        return self.__score
