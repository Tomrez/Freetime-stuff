import pygame
import time


import G_vars as Gs
from player import Player
from ghost import Ghost
import borders

class Board():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('PacMan')
        self.time = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Gs.WIDTH, Gs.HEIGHT))
        self.borders = borders.borders
        self.player = Player()
        
        # Ghosts with specific spawn points
        self.ghosts = []
        self.ghosts.append(Ghost(1, 1))
        self.ghosts.append(Ghost(Gs.TOP_INDEX + 1, Gs.RIGHT_INDEX - 1))
        self.ghosts.append(Ghost(Gs.BOTTOM_INDEX - 1, 1))
        self.ghosts.append(Ghost(Gs.BOTTOM_INDEX - 1, Gs.RIGHT_INDEX - 1))

        self.last_move_time = time.time()


    def draw_square(self, x, y, color=Gs.GRID_COLOR):
        pygame.draw.rect(self.screen, color, (x * Gs.BLOCK, y * Gs.BLOCK, Gs.BLOCK, Gs.BLOCK))


    def draw_borders(self):
        for i in range(Gs.BLOCKS_HEIGHT):
            for j in range(Gs.BLOCKS_WIDTH):
                if self.borders[i][j] == 1:
                    self.draw_square(j, i)


    def draw_objects(self):
        # Draw pacman
        self.draw_square(self.player.x, self.player.y, Gs.PACMAN_COLOR)

        # Draw ghosts
        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                self.draw_square(ghost.x, ghost.y, Gs.GHOST_COLOR)


    def is_time_to_move(self):
        curr_time = time.time()

        if curr_time - self.last_move_time * Gs.STEP_TIME:
            self.last_move_time = curr_time
            return True
        return False
