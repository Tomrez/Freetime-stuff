

class Ghost():
    def __init__(self, y:int, x:int) -> None:
        self.x = x
        self.y = y
        self.previous_x = None
        self.previous_y = None