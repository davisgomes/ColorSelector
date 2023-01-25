import pygame
import menumode
import playmode
import failmode


# Constants that hold the game state
MENU = 0
PLAY = 1
FAIL = 2
NUM_STATES = 3


# Game defines a game object that manages the game state
# and controls game mechanics
class Game:
    def __init__(self):
        # initialize game variables
        self.exit = False
        self.canvas = pygame.display.set_mode((500, 500))
        self.game_state = MENU
        self.scores = []
        self.states = {
            MENU: menumode.MenuMode(self.canvas),
            PLAY: playmode.PlayMode(self.canvas),
            FAIL: failmode.FailMode(self.canvas)
        }

        # initialize game settings
        pygame.init()
        pygame.display.set_caption("Color Selector")

    # run_game sets the game loop and starts the display
    def run_game(self):
        while not self.exit:
            self.run_display()

    # run_display selects the display based on the game state
    # The states are in circular order:
    #   MENU
    #   PLAY
    #   FAIL
    def run_display(self):
        self.scores = self.states[self.game_state].run(self.scores)
        self.game_state = (self.game_state + 1) % NUM_STATES

