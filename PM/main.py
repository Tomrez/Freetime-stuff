import pygame


from board import Board
import G_vars as Gs
from actions import Actions

def main():

    board = Board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if board.is_time_to_move():
            Actions.move(board)


        board.screen.fill(Gs.BG_COLOR)
        board.draw_borders()
        board.draw_objects()



        pygame.display.flip()



if __name__ == '__main__':
    main()      