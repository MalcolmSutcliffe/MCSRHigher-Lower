import Data
from Data import *
from Game import Game

if __name__ == '__main__':
    Data.initialize_data()
    new_game = Game()
    new_game.play()


