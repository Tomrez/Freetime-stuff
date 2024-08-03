
#COLOR DEFINITIONS
BG_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
OBJECT_COLOR = (0, 0, 200)

# SIZE OF THE SCREEN
WIDTH = 400
HEIGHT = 800
#SIZE OF BLOCK -> WIDTH/BLOCK x HEIGHT/BLOCK big screen
BLOCK = 40
BLOCK_WIDTH = WIDTH // BLOCK
BLOCK_HEIGHT = HEIGHT // BLOCK

# Each step takes STEP_TIME
STEP_TIME = 1

# Object will appear at the x[START_X_POS] when spawned
START_X_POS = 4
# Object will appear at the y[START_Y_POS] when spawned
START_Y_POS = 0


# Better keep lower, because of problems when reading keyboard input
FPS = 16


# BORDERS - inclusive
LEFT_INDEX = 0
RIGHT_INDEX = 9
TOP_INDEX = 0
BOTTOM_INDEX = 19