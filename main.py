import Data
from Game import Game
from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=8080, debug=True)
    Data.initialize_data()
    new_game = Game()
    is_running = True
    while is_running:
        user_input = input("Play a game?: y/n \n")
        if not user_input:
            print("unknown input. Try again")
            continue
        if user_input[0] == "n":
            print("okay, bye!")
            is_running = False
            break
        elif user_input[0] != "y":
            print("unknown input. Try again")
            continue
        new_game.play()
