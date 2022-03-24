import Data
from Game import Game

if __name__ == '__main__':
    Data.initialize_data()
    new_game = Game()
    is_running = True
    while is_running:
        user_input = input("Play a game?: y/n \n")
        if user_input[0] == "n":
            print("okay, bye!")
            is_running = False
            break
        elif user_input[0] != "y":
            print("unknown input. Try again")
            continue
        new_game.play()


