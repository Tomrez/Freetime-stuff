import pygame


from board import Board
import G_vars as Gs
from actions import Actions

def main():

    board = Board()
    actions = Actions()

    previous_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for any keyboard input
        actions.handle_input(board)        

        if board.is_time_to_move():
            actions.move(board)

        if board.is_time_to_spawn_coin():
            actions.spawn_coin(board)

        if actions.does_step_on_coin(board):
            actions.get_coin(board)

        if board.player.score != previous_score:
            print(board.player.score)
            previous_score = board.player.score

        board.screen.fill(Gs.BG_COLOR)
        board.draw_borders()
        board.draw_coins()
        board.draw_objects()

        pygame.display.flip()
        board.time.tick(Gs.FPS)


if __name__ == '__main__':
    main()      