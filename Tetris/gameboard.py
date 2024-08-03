import pygame
import numpy
import random
import time

import G_vars
from object import Object
from enums import Shapes


class Board():

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.time = pygame.time.Clock()
        self.screen = pygame.display.set_mode((G_vars.WIDTH, G_vars.HEIGHT))
        self.filled_squares = numpy.zeros((20, 10))
        new_shape = self.get_new_shape()
        self.active_object = Object(new_shape)
        self.last_move_time = time.time()


    # Function returns random shape from shapes enum
    def get_new_shape(self) -> list:
        shapes = Shapes()
        random.seed(a=None, version=2)
        index = random.randint(0, 66666) % len(shapes.shapes)
        shape = shapes.shapes[index].copy()
        return shape


    # Function draw grid on the screen
    def draw_grid(self):
        for x in range(0, G_vars.WIDTH, G_vars.BLOCK):
            pygame.draw.line(self.screen, G_vars.GRID_COLOR, (x, 0), (x, G_vars.HEIGHT))
        for y in range(0, G_vars.HEIGHT, G_vars.BLOCK):
            pygame.draw.line(self.screen, G_vars.GRID_COLOR, (0, y), (G_vars.WIDTH, y))


    # Function to draw single squares
    def draw_square(self, x, y, color):
        pygame.draw.rect(self.screen, G_vars.OBJECT_COLOR, (x * G_vars.BLOCK, y * G_vars.BLOCK, G_vars.BLOCK, G_vars.BLOCK))


    # Function to draw active object
    def draw_object(self):
        for coord in self.active_object.shape:
            self.draw_square(coord[0], coord[1], G_vars.OBJECT_COLOR)


    # Function draw already placed objects
    def draw_placed_objects(self):
        for i in range(20):
            for j in range(10):
                if self.filled_squares[i][j] == 1:
                    self.draw_square(j, i, G_vars.OBJECT_COLOR)


    # Function to check, if the STEP_TIME already expired and is time to move
    def is_time_to_move(self) -> bool:
        curr_time = time.time()

        if curr_time - self.last_move_time > G_vars.STEP_TIME:
            self.last_move_time = curr_time
            return True
        
        return False
