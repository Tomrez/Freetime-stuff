from board import Board
from ghost import Ghost
import G_vars as Gs

import random
import pygame

class Actions():

    def handle_input(self, board:Board):
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.arr_left(board)
        elif pressed[pygame.K_RIGHT]:
            self.arr_right(board)
        elif pressed[pygame.K_UP]:
            self.arr_up(board)
        elif pressed[pygame.K_DOWN]:
            self.arr_down(board)

    
    def arr_left(self, board:Board):
        
        if not self.hit_wall(board, board.player.x - 1, board.player.y):
            board.player.x -= 1
            if self.does_hit_ghost(board):
                board.player.decrease_score()

    def arr_right(self, board:Board):
        
        if not self.hit_wall(board, board.player.x + 1, board.player.y):
            board.player.x += 1
            if self.does_hit_ghost(board):
                board.player.decrease_score()

    def arr_up(self, board:Board):
        
        if not self.hit_wall(board, board.player.x, board.player.y - 1):
            board.player.y -= 1
            if self.does_hit_ghost(board):
                board.player.decrease_score()

    def arr_down(self, board:Board):
        
        if not self.hit_wall(board, board.player.x, board.player.y + 1):
            board.player.y += 1
            if self.does_hit_ghost(board):
                board.player.decrease_score()


    def spawn_coin(self, board:Board):
        
        random.seed(a=None, version=2)
        spawned = False

        while not spawned:
            x_coord = random.randint(0, Gs.RIGHT_INDEX)
            y_coord = random.randint(0, Gs.BOTTOM_INDEX)
            if not self.hit_wall(board, x_coord, y_coord):
                board.coins[y_coord][x_coord] = 1
                spawned = True


    def get_coin(self, board:Board):
        
        board.coins[board.player.y][board.player.x] = 0
        board.player.increase_score()


    def does_step_on_coin(self, board:Board) -> bool:
        
        if board.coins[board.player.y][board.player.x] == 1:
            return True
        return False      


    def does_hit_ghost(self, board:Board) -> bool:
        
        for ghost in board.ghosts:
            if isinstance(ghost, Ghost):
                if board.player.x == ghost.x and board.player.y == ghost.y:
                    return True
        return False      
    

    def move(self, board:Board):

        for ghost in board.ghosts:

            if isinstance(ghost, Ghost):

                new_place = False
                random.seed(a=None, version=2)
       
                atempt_cnt = 0

                # Handle situation, when ghost got stuck in corner with three walls, so only option is goin back to the previous square
                while not new_place:
                    atempt_cnt += 1
                    if atempt_cnt > 30:
                        ghost.x = ghost.previous_x
                        ghost.y = ghost.previous_y
                        new_place = True

                    match random.randint(0, 66666) % 4:
                        case 0:
                            #TOP
                            if ghost.y - 1 != ghost.previous_y and not self.hit_wall(board, ghost.x, ghost.y - 1):
                                ghost.previous_y = ghost.y
                                ghost.previous_x = ghost.x
                                ghost.y -=  1
                                new_place = True
                        case 1:
                            # RIGHT
                            if ghost.x + 1 != ghost.previous_x and not self.hit_wall(board, ghost.x + 1, ghost.y):
                                ghost.previous_y = ghost.y
                                ghost.previous_x = ghost.x
                                ghost.x += 1
                                new_place = True

                        case 2:
                            # BOTTOM
                            if ghost.y + 1 != ghost.previous_y and not self.hit_wall(board, ghost.x, ghost.y + 1):
                                ghost.previous_y = ghost.y
                                ghost.previous_x = ghost.x
                                ghost.y += 1
                                new_place = True

                        case 3:
                            # LEFT
                            if ghost.x - 1 != ghost.previous_x and not self.hit_wall(board, ghost.x - 1, ghost.y):
                                ghost.previous_y = ghost.y
                                ghost.previous_x = ghost.x
                                ghost.x -= 1
                                new_place = True
        if self.does_hit_ghost(board):
            board.player.decrease_score()


    def hit_wall(self, board:Board, x:int, y:int):
        if board.borders[y][x] == 1:
            return True
        return False
        