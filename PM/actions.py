from board import Board
from ghost import Ghost

import random

class Actions():



    def move(board:Board):
        #TODO Move ghosts
        #TODO Can just get random direction, which square is not the same as the previous one
        #TODO That should make random movement without just goin back and forth
        #! Maybe check, if player moved in the time and if not, do somethin

        for ghost in board.ghosts:
            if isinstance(ghost, Ghost):
                ghost.previous_x = ghost.x
                ghost.previous_y = ghost.y

                new_place = False

                while not new_place:
                    direct = random.randint(0, 3)
                    match direct:
                        case 0:
                            #TOP
                            if ghost.y - 1 != ghost.previous_y:
                                ghost.y = direct
                                new_place = True
                        case 1:
                            # RIGHT
                            if ghost.x + 1 != ghost.previous_y:
                                ghost.x = direct
                                new_place = True

                        case 2:
                            # BOTTOM
                            if ghost.y + 1 != ghost.previous_y:
                                ghost.y = direct
                                new_place = True

                        case 3:
                            # LEFT
                            if ghost.x - 1 != ghost.previous_y:
                                ghost.x = direct
                                new_place = True
