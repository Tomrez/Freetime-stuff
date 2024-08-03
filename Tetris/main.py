import pygame

from gameboard import Board
from actions import Actions
import G_vars


def main():

    #Inicialize board and actions
    board = Board()
    actions = Actions()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for any keyboard input
        actions.handle_input(board)

        # Move if the time is up
        if board.is_time_to_move() == True:
            actions.move(board)

        # Draw
        board.screen.fill(G_vars.BG_COLOR)
        board.draw_grid()
        board.draw_placed_objects()
        board.draw_object()

        # Turn on display
        pygame.display.flip()
        board.time.tick(G_vars.FPS)

                    
if __name__ == "__main__":
    main()
            