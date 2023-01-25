import pygame
import blockarrayclass


# Mode class is the generic class for each game mode
# it defines the shared functions between each mode
class Mode:
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.block_array = blockarrayclass.BlockArray(self.canvas)
        self.run_mode = True

    # run displays the game mode
    def run(self, scores):
        return scores

    # check events checks to see if the events have been processed
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit(0)

    # display_text displays white text that is centered on screen
    # the height and size of the text can be modified
    def display_text(self, t="", text_size=32, height=0):
        font = pygame.font.SysFont(None, text_size)
        text = font.render(t, True, pygame.Color(255, 255, 255))
        self.canvas.blit(text, (self.canvas.get_width() / 2 - text.get_width() / 2,
                                self.canvas.get_height() / 2 - text.get_height() / 2 + height))

    # clear screen fills the screen with black to remove all contents form the screen
    def clear_screen(self):
        self.canvas.fill(pygame.Color(0, 0, 0))
