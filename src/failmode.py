import pygame
import modeclass
import blockarrayclass
import helpers


# FailMode is a class that contains the display for a game failure
class FailMode(modeclass.Mode):
    def __init__(self, canvas):
        super().__init__(canvas)

    # run displays the fail screen with the most recent user score
    def run(self, scores):
        self.run_mode = True
        menu_color = helpers.random_color(0, helpers.MAX_DIFFERENCE)
        self.block_array = blockarrayclass.BlockArray(self.canvas, 2, menu_color, helpers.MAX_DIFFERENCE)

        while self.run_mode:
            self.block_array.display_blocks()
            self.display_text("You have selected the wrong square", 32, -100)
            self.display_text("Score: " + str(scores[-1]), 32, -50)
            self.display_text("Click the different color to return to the menu", 24, 100)
            self.check_events()
            pygame.display.flip()

        return scores

    # check_events determines if the correct block was clicked
    # if so, we stop the fail mode display
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.block_array.check_mouse_press():
                self.clear_screen()
                self.run_mode = False
        super().check_events()
