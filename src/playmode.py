import copy
import pygame
import modeclass
import blockarrayclass
import helpers


# PlayMode is a class that contains the play mode
class PlayMode(modeclass.Mode):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.level = 0
        self.scores = []

    # run creates a new block array on screen and
    # keeps track of the current player score
    def run(self, scores):
        self.run_mode = True
        self.scores = copy.deepcopy(scores)
        self.set_calculated_block_array()

        while self.run_mode:
            self.block_array.display_blocks()
            self.check_events()
            pygame.display.flip()
        return self.scores

    # check_events increases the score if the user selects the correct square
    # otherwise, the play mode is ended
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.block_array.check_mouse_press():
                    self.set_calculated_block_array()
                    self.level += 1
                else:
                    self.scores.append(self.level)
                    self.level = 0
                    self.run_mode = False
                self.clear_screen()
        super().check_events()

    # set_calculated_block_array returns a block array with an increasingly difficult color and number of blocks
    # The color difference diminishes with the level and the block size increases at helpers.BLOCK_CHANGE_LEVELS
    def set_calculated_block_array(self):
        play_color = helpers.random_color()
        calculated_diff = max(helpers.MAX_DIFFERENCE - self.level * helpers.COLOR_CHANGE_LEVELS, helpers.MIN_DIFFERENCE)
        calculated_num_blocks = min(helpers.MIN_BLOCKS + self.level // helpers.BLOCK_CHANGE_LEVELS, helpers.MAX_BLOCKS)
        self.block_array = blockarrayclass.BlockArray(self.canvas, calculated_num_blocks, play_color, calculated_diff)
