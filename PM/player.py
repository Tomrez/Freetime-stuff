
import G_vars as Gs

class Player():

    def __init__(self) -> None:
        self.x = 25
        self.y = 12
        self.color = Gs.PACMAN_COLOR
        self.score = 0


    def increase_score(self) -> None:
        self.score += Gs.INC_POINTS

    def decrease_score(self) -> None:
        self.score -= Gs.DCS_POINTS

    def move_to(self, x:int, y:int) -> None:
        self.x = x
        self.y = y