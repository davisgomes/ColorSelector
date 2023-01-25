import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import gameclass


# run_game creates a game object and runs the game
def run_game():
    new_game = gameclass.Game()
    new_game.run_game()


if __name__ == '__main__':
    run_game()
