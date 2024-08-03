
class Shapes():
    def __init__(self) -> None:
        self.shapes = (
            [[4, 0], [5, 0], [6, 0], [7, 0], [7, 1]], # Long L
            [[4, 0], [5, 0], [6, 0], [6, 1]], # Short L
            [[4, 0], [5, 0], [6, 0], [7, 0]], # Long I
            [[4, 0], [5, 0], [6, 0]], # Shorter I
            [[4, 0], [5, 0]], # Shortest I
            [[4, 0], [5, 0], [6, 0], [4, 1], [5, 1]], # B shape
            [[4, 0], [5, 0], [4, 1], [5, 1]], # O shape
            [[5, 0], [6, 0], [4, 1], [5, 1]], # Z shape
            [[4, 0], [5, 0], [6, 0], [5, 1]] # T shape

        )


class Colors():
    def __init__(self) -> None:
        self.colors = (
            (255, 0, 0), # Red
            (0, 255, 0), # Green
            (0, 0, 255), # Blue
            (255, 255, 0), # Yellow
            (255, 0, 255), # Purple
            (0, 255, 255) # Cyan
        )