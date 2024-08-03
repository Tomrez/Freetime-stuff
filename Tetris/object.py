import G_vars


class Object():
    def __init__(self, shape:list, color) -> None:
        self.x_pos = G_vars.START_X_POS
        self.y_pos = G_vars.START_Y_POS
        self.num_of_blocks = len(shape)
        self.times_rotated = 0
        self.shape = shape
        self.color = color