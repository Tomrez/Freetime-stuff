import time
import pygame
import numpy

from gameboard import Board
from object import Object
import G_vars


class Actions():

    def handle_input(self, board:Board):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.arr_left(board)
        elif pressed[pygame.K_RIGHT]:
            self.arr_right(board)
        elif pressed[pygame.K_UP]:
            self.arr_up(board)
        elif pressed[pygame.K_DOWN]:
            self.arr_down(board)

    
    def move_placed_objects(self, board:Board):
        for i in range(18, -1, -1):
            for j in range(10):
                if board.filled_squares[i + 1][j] == 0 and board.filled_squares[i][j] == 1:
                    #If there is no square under placed square, move square one line down
                    board.filled_squares[i][j] = 0
                    board.filled_squares[i + 1][j] = 1

                    board.filled_squares_colors[i+1][j] = board.filled_squares_colors[i][j]
                    board.filled_squares_colors[i][j] = 0


    def is_complete_line(self, board:Board) -> bool:
        for line in board.filled_squares:
            # If complete line was filled
            if numpy.all(line):
                return True
        return False
                

    def delete_complete_line(self, board:Board):
        for i in range(G_vars.BOTTOM_INDEX + 1):
            if numpy.all(board.filled_squares[i]):
                for j in range(10):
                    board.filled_squares[i][j] = 0


    def can_move_there(self, board:Board, wanted_y:int, wanted_x:int):
        if board.filled_squares[wanted_x][wanted_y] == 1:
            return False
        else:
            return True


    def arr_down(self, board:Board):
        self.active_object_down(board)


    def arr_up(self, board:Board):
        # TODO
        return
        # Rotace objektu o 90 stupnu (doprava)
        x = board.active_object.x_pos
        y = board.active_object.y_pos

        cut_submatrix = board.filled_squares[x:x+4, y:y+4]
        new_submatrix = numpy.rot90(cut_submatrix, -1)
        board.filled_squares[x:x+4, y:y+4] = new_submatrix


    # Function move object to the left after keyboard left arrow input
    def arr_left(self, board:Board):
        # Check if is possible to move left
        for coord in board.active_object.shape:
            if coord[0] <= G_vars.LEFT_INDEX or self.can_move_there(board, coord[0] - 1, coord[1]) == False:
                return 
            
        for coord in board.active_object.shape:
            coord[0] -= 1
        board.active_object.x_pos -= 1
        time.sleep(0.1)


    # Function move object to the right agter keyboard right arrow input
    def arr_right(self, board:Board):
        # Check if is possible to move right
        for coord in board.active_object.shape:
            if coord[0] >= G_vars.RIGHT_INDEX or self.can_move_there(board, coord[0] + 1, coord[1]) == False:
                return 
            
        for coord in board.active_object.shape:
            coord[0] += 1
        board.active_object.x_pos += 1
        time.sleep(0.1)


    # Set object as inactive, after fall all the way to the bottom
    def set_object_inactive(self, board:Board):
        object_to_destroy = board.active_object
        matrix_to_add = board.filled_squares
        color_matrix_to_add = board.filled_squares_colors
        for coord in object_to_destroy.shape:
            matrix_to_add[coord[1]][coord[0]] = 1
            color_matrix_to_add[coord[1]][coord[0]] = board.active_object.color


    # Move the current falling object down
    def active_object_down(self, board:Board):
        # If object get to the bottom, set it as inactive and spawn new one
        for coord in board.active_object.shape:
            if coord[1] >= G_vars.BOTTOM_INDEX or self.can_move_there(board, coord[0], coord[1] + 1) == False:
                self.set_object_inactive(board)
                new_shape = board.get_new_shape()
                new_color = board.get_new_color()
                board.active_object = Object(new_shape, new_color)
                self.is_game_over(board)
                return

        for coord in board.active_object.shape:
            coord[1] += 1
        board.active_object.y_pos += 1


    # Check if squares get all the way to the top
    def is_game_over(self, board:Board):
        for square in board.filled_squares[0]:
            if square == 1:
                print('Game over :(')
                exit()
        

    # Move all object, which can move
    def move(self, board:Board):
        if self.is_complete_line(board) == True:
            self.delete_complete_line(board)
            self.move_placed_objects(board)

        self.active_object_down(board)