import copy
import pygame
import random

BORDER = 3


# BlockArray creates an array of color blocks, selecting one block to be different
# This class draws the display for the array of blocks that gets created on screen
class BlockArray:
    def __init__(self, canvas, block_num=2, base_color=pygame.Color(0, 0, 0), color_diff=0):
        # initialize class variables for display
        self.canvas = canvas
        self.block_num = block_num
        self.base_color = base_color
        self.special_block = random.randint(0, self.block_num**2 - 1)
        self.color_diff = color_diff
        self.diffr, self.diffg, self.diffb = self.color_decomposition()

        # block characteristics
        canvas_width = self.canvas.get_width()
        canvas_height = self.canvas.get_height()
        self.block_width = canvas_width/self.block_num - BORDER
        self.block_height = canvas_height/self.block_num - BORDER

    # display_blocks draws the array of blocks on screen and selects the "special" block
    def display_blocks(self):
        for i in range(self.block_num):
            for j in range(self.block_num):
                x = i * (self.block_height + BORDER)
                y = j * (self.block_width + BORDER)

                display_color = self.base_color
                if i * self.block_num + j == self.special_block:
                    display_color = self.change_block_color()
                pygame.draw.rect(self.canvas, display_color, pygame.Rect(x, y, self.block_width, self.block_height))

    # change_block_color changes the color of the rgb block values based on the calculated difference
    def change_block_color(self):
        new_color = copy.deepcopy(self.base_color)
        new_color.r = self.color_val(new_color.r, self.diffr)
        new_color.g = self.color_val(new_color.g, self.diffg)
        new_color.b = self.color_val(new_color.b, self.diffb)
        return new_color

    # color val computes a difference without overflowing the rgb values
    def color_val(self, curr, diff):
        if curr + diff < 0 or curr + diff > 255:
            diff = -diff
        return curr + diff

    # color_decomposition calculates diffs for the reg green and blue values evenly distributed by the color_diff
    def color_decomposition(self):
        remaining_value = self.color_diff
        r = random.randint(0, remaining_value)
        remaining_value -= r
        g = random.randint(0, remaining_value)
        remaining_value -= g
        b = random.randint(0, remaining_value)
        remaining_value -= b
        return r, g, b

    # check_mouse_press determines if the mouse press was on the correct square
    # it will return true if so and false otherwise
    def check_mouse_press(self):
        x, y = pygame.mouse.get_pos()

        i = self.special_block // self.block_num
        j = self.special_block % self.block_num

        min_x = i * (self.block_width + BORDER)
        min_y = j * (self.block_height + BORDER)
        max_x = min_x + self.block_width
        max_y = min_y + self.block_height

        if min_x < x < max_x and min_y < y < max_y:
            return True
        return False
