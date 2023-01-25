import pygame
import copy
import modeclass
import blockarrayclass
import helpers

MAX_DIFFERENCE = 255//2


# MenuMode is a class that contains the menu mode
class MenuMode(modeclass.Mode):
    def __init__(self, canvas):
        super().__init__(canvas)

    # run displays the menu screen
    def run(self, scores):
        self.run_mode = True
        menu_color = helpers.random_color(0, MAX_DIFFERENCE)
        self.block_array = blockarrayclass.BlockArray(self.canvas, 2, menu_color, MAX_DIFFERENCE)

        while self.run_mode:
            self.block_array.display_blocks()
            self.display_text("Color Selector Game", 52, -100)
            self.display_text("Select the square that has a different color", 24, 100)
            self.display_text("Select the different color to start", 18, 125)
            self.display_text("High Score: " + str(helpers.get_high_score(copy.deepcopy(scores))), 32, -50)
            self.check_events(pygame.event.get())
            pygame.display.flip()

        return scores

    # check_events checks to make sure the mouse is pressed on the correct square
    # if this is the case, the menu will close
    def check_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.block_array.check_mouse_press():
                self.clear_screen()
                self.run_mode = False
        super().check_events(events)
