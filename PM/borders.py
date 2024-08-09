import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)

import G_vars as Gs


#TODO Napad: Udelat par polopruhlednych bloku, kterymy nemuzou projit duchove ale pouze hrac

borders = numpy.zeros((Gs.BLOCKS_HEIGHT, Gs.BLOCKS_WIDTH))

borders[0] = 1
borders[Gs.BOTTOM_INDEX] = 1

for i in range(Gs.BLOCKS_HEIGHT):
    borders[i][0] = 1
    borders[i][Gs.RIGHT_INDEX] = 1


for i in range(15):
    # Left U
    borders[5][i + 5] = 1
    borders[15][i + 5] = 1

    # Right U
    borders [5][i + 30] = 1
    borders [15][i + 30] = 1


for i in range(11):
    # Left U
    borders[i + 5][20] = 1
    # Right U
    borders[i + 5][30] = 1
