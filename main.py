import Data
from Game import Game
from website import create_app

app = create_app()

if __name__ == '__main__':
    # Data.verify_data()
    # app.run(debug=True)
    Data.initialize_data()
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
        new_game = Game()
        new_game.play()
