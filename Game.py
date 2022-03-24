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
        print("-"*(12 + len(str(self.__score + 1))))
        print("| ROUND: " + str(self.__score + 1) + " |")
        print("-"*(12 + len(str(self.__score + 1))))
        print(self.__clue_one["name"] + " with a time of: " + str(self.__clue_one["time"])
              + " is higher or lower than: " + self.__clue_two["name"] + "?")
        while self.__is_running:
            var = input("h/l:")
            if var[0] != "h" and var[0] != "l":
                print("unrecognized guess, try again")
                continue
            if var[0] == "h" and self.__clue_one["time"] >= self.__clue_two["time"]:
                self.correct_guess("higher")
                break
            elif var[0] == "l" and self.__clue_one["time"] <= self.__clue_two["time"]:
                self.correct_guess("lower")
                break
            elif var[0] == "h":
                self.incorrect_guess("higher")
                break
            elif var[0] == "l":
                self.incorrect_guess("lower")
                break

            print("unrecognized guess, try again")

    def __get_next_value(self):
        if len(self.__game_order) == 0:
            self.game_won()
            return
        return self.__game_order.pop()

    def correct_guess(self, guess_type):
        print("correct! " + self.__clue_one["name"] + " has a " + guess_type + " time than "
              + self.__clue_two["name"] + " with: " + str(self.__clue_two["time"]))
        self.__score = self.__score + 1
        self.__clue_one = self.__clue_two
        self.__clue_two = self.__get_next_value()
        self.play_round()

    def incorrect_guess(self, guess_type):
        print("incorrect! " + self.__clue_one["name"] + " does not have a " + guess_type + " time than "
              + self.__clue_two["name"] + " with: " + str(self.__clue_two["time"]))
        self.game_lost()

    def game_won(self):
        print("Congrats! You win 0.o")
        self.__is_running = False

    def game_lost(self):
        print("You Lost!")
        self.__is_running = False

    def get_is_running(self):
        return self.__is_running

    def get_clue_one(self):
        return copy.copy(self.__clue_one)

    def get_clue_two(self):
        return copy.copy(self.__clue_two)

    def get_score(self):
        return self.__score
