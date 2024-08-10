import pygame
import time
import numpy
import math


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
        self.ghosts.append(Ghost(Gs.GHOST1_X, Gs.GHOST1_Y))
        self.ghosts.append(Ghost(Gs.GHOST2_X, Gs.GHOST2_Y))
        self.ghosts.append(Ghost(Gs.GHOST3_X, Gs.GHOST3_Y))
        self.ghosts.append(Ghost(Gs.GHOST4_X, Gs.GHOST4_Y))

        self.coins = numpy.zeros((Gs.BLOCKS_HEIGHT, Gs.BLOCKS_WIDTH))

        self.last_move_time = time.time()
        self.last_coin_time = time.time()


    def draw_square(self, x, y, color, borders = False, coin = False, ghosts = False, pacman=False):

        if borders:
            pygame.draw.rect(self.screen, Gs.GRID_COLOR, (x * Gs.BLOCK, y * Gs.BLOCK, Gs.BLOCK, Gs.BLOCK), width=2)

        if coin:
            center_x = x * Gs.BLOCK + Gs.BLOCK // 2
            center_y = y * Gs.BLOCK + Gs.BLOCK // 2
            radius = Gs.BLOCK // 4 
            pygame.draw.circle(self.screen, Gs.COIN_COLOR, (center_x, center_y), radius)

        if ghosts:
            # BASE
            center_x = x * Gs.BLOCK + Gs.BLOCK // 2
            center_y = y * Gs.BLOCK + Gs.BLOCK // 2
            radius = Gs.BLOCK // 2

            pygame.draw.circle(self.screen, color, (center_x, center_y - radius // 2), radius)
            pygame.draw.rect(self.screen, color, (center_x - radius, center_y - radius // 2, radius * 2, radius))

            # BOTTOM
            wave_radius = radius // 3
            for i in range(3):
                wave_center_x = center_x - radius + wave_radius + (wave_radius * 2 * i)
                wave_center_y = center_y + radius // 2
                pygame.draw.circle(self.screen, color, (wave_center_x, wave_center_y), wave_radius)
    
            # EYES
            eye_radius = radius // 4
            eye_offset_x = radius // 3
            eye_offset_y = radius // 4
            pygame.draw.circle(self.screen, (255, 255, 255), (center_x - eye_offset_x, center_y - eye_offset_y), eye_radius)
            pygame.draw.circle(self.screen, (255, 255, 255), (center_x + eye_offset_x, center_y - eye_offset_y), eye_radius)

            # INSIDE EYES
            pupil_radius = eye_radius // 2
            pupil_offset_x = radius // 6
            pupil_offset_y = radius // 8
            pygame.draw.circle(self.screen, (0, 0, 0), (center_x - eye_offset_x + pupil_offset_x, center_y - eye_offset_y + pupil_offset_y), pupil_radius)
            pygame.draw.circle(self.screen, (0, 0, 0), (center_x + eye_offset_x + pupil_offset_x, center_y - eye_offset_y + pupil_offset_y), pupil_radius)


        if pacman:

            center_x = x * Gs.BLOCK + Gs.BLOCK // 2
            center_y = y * Gs.BLOCK + Gs.BLOCK // 2
            radius = Gs.BLOCK // 2

            # BODY
            pygame.draw.circle(self.screen, color, (center_x, center_y), radius)

            # MOUTH
            mouth_angle_rad = math.radians(30)
            start_x = center_x + radius * math.cos(mouth_angle_rad)
            start_y = center_y - radius * math.sin(mouth_angle_rad)

            end_x = center_x + radius * math.cos(-mouth_angle_rad)
            end_y = center_y - radius * math.sin(-mouth_angle_rad)

            pygame.draw.polygon(self.screen, (0, 0, 0), [(center_x, center_y), (start_x, start_y), (end_x, end_y)])

                    


    def draw_borders(self):
        for i in range(Gs.BLOCKS_HEIGHT):
            for j in range(Gs.BLOCKS_WIDTH):
                if self.borders[i][j] == 1:
                    self.draw_square(j, i, Gs.BG_COLOR, borders=True)

    
    def draw_coins(self):
        for i in range(Gs.BLOCKS_HEIGHT):
            for j in range(Gs.BLOCKS_WIDTH):
                if self.coins[i][j] == 1:
                    self.draw_square(j, i, Gs.BG_COLOR, coin=True)


    def draw_objects(self):
        # Draw pacman
        self.draw_square(self.player.x, self.player.y, Gs.PACMAN_COLOR, pacman=True)

        # Draw ghosts
        for ghost in self.ghosts:
            if isinstance(ghost, Ghost):
                self.draw_square(ghost.x, ghost.y, Gs.GHOST_COLOR, ghosts=True)


    def is_time_to_move(self) -> bool:
        curr_time = time.time()

        if curr_time - self.last_move_time > Gs.STEP_TIME:
            self.last_move_time = curr_time
            return True
        return False
    
    
    def is_time_to_spawn_coin(self) -> bool:
        curr_time = time.time()

        if curr_time - self.last_coin_time > Gs.SPAWN_COIN_TIME:
            self.last_coin_time = curr_time
            return True
        return False
