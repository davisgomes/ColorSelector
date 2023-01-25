import pygame
import random

# Constants for game mechanics
MAX_DIFFERENCE = 255 // 2
MIN_DIFFERENCE = 4
MAX_BLOCKS = 5
MIN_BLOCKS = 2
COLOR_CHANGE_LEVELS = 2
BLOCK_CHANGE_LEVELS = 15


# random_color returns a randomly initialized pygame color within a given rgb range
def random_color(min_r=0, max_r=255):
    return pygame.Color(random.randint(min_r, max_r), random.randint(min_r, max_r), random.randint(min_r, max_r))


# get_high_score returns the highest score from a list of scores
def get_high_score(scores):
    if len(scores) == 0:
        return 0
    scores.sort()
    return scores[-1]
