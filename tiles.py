

    ### This code uses inputted dimensions for a rectangular room and a
    ### rectangular tile, and outputs the number of tiles needed to tile the
    ### room optimally. It then outputs 


## This section uses the inputted x and y dimensions for the room and tile
## to give the number of tiles required for the optimal layout, in a
## rectangular room.

import sys

Lx, Ly, runits = float(input("Dimensions of room: ")), float(input("by: ")), raw_input("type metres or feet: ")
                                          # Input dimensions of room.

if runits == 'metres' or runits == 'feet':
    print " "
else:
    sys.exit("Type allowed units")
                                          # Breaks if invalid units are inputted.
    
lx, ly, tunits = float(input("Dimensions of tile: ")), float(input("by: ")), raw_input("type centimetres or inches: ") 
                                          # Input dimensions of tile.
if tunits == 'centimetres' or tunits == 'inches':
    print " "
else:
    sys.exit("Type allowed units")
                                          # Breaks if invalid units are inputted.
    
if runits == 'metres' and tunits == 'centimetres':
    lx = 0.01 * lx    
    ly = 0.01 * ly    
    funits = 'metres'
elif runits == 'feet' and tunits == 'inches':
    lx = 0.08384 * lx    
    ly = 0.08384 * ly    
    funits = 'feet'
elif runits == 'metres' and tunits == 'inches':
    lx = 0.0254 * lx    
    ly = 0.0254 * ly
    funits = 'metres'
elif runits == 'feet' and tunits == 'centimetres':
    lx = 0.03281 * lx    
    ly = 0.03281 * ly
    funits = 'feet'

                                          # Converts the dimensions of the tile
                                          # into those of the room, and then 
                                          # defines funits to be the units with
                                          # which we work with henceforth.

nxa = int(Lx / lx - 1)
nya = int(Ly / ly - 1)                    # Number of tiles needed in x 
                                          # and y directions.

Na = (nxa + 2) * (nya + 2)                # Total number of tiles needed.

nxb = int(Lx / ly - 1)
nyb = int(Ly / lx - 1)
    
Nb = int(nxb + 2.0) * int(nyb + 2.0)      # Repeat for opposite alignment
                                          # of tiles.
  
if Nb < Na:
    N = Nb
    temp = lx
    lx = ly
    ly = temp
    nx = nxb
    ny = nyb                          
else:
    N = Na
    nx = nxa
    ny = nya
                                          # Choose optimal alignment. If 
                                          # opposite alignment is optimal, lx
                                          # and ly switch. The number of tiles
                                          # needed in each direction are 
                                          # defined as nx and ny.

print (" ")    

print N, 'tiles needed'

## This section uses the inputted x and y dimensions for the room and tile
## to give an image of the tiled room.

from PIL import Image

import numpy as np

X, Y, x, y = int(round(100*Lx)), int(round(100*Ly)), int(round(100*lx)), int(round(100*ly))
                                          # Images require an integer number of
                                          # pixels, since I want the number of
                                          # pixels to be proportional to the 
                                          # size of the room, I am defining 
                                          # these new numbers to be the
                                          # dimensions of the room and tile, 
                                          # but with units of 'pixels' instead  
                                          # of metres.

rx = int(0.5*(X-(nx*x)))

ry = int(0.5*(Y-(ny*y)))

                            
rimg = np.empty((X,Y),np.uint32)          # Uses the room dimensions to create
                                          # an empty array.

rimg.shape=Y,X                            # Sets the size of the array to be
                                          # X by Y.

rimg[0:Y:,0:X]=0xFFFFFFFF                 # Turns the empty pixels into white
                                          # pixels. The eight values are
                                          # hexidecimal numbers in the format
                                          # 0xAABBGGRR, where B, G, and R are
                                          # blue, green and red respectively,
                                          # while A is transparency. FF is the
                                          # highest possible value (255), so 
                                          # FFFFFFFF gives a solid white pixel.

rimg[ry:(Y-ry),0:rx]=0xFF00FF00

rimg[ry:(Y-ry),(X-rx):X]=0xFF00FF00

rimg[0:ry,rx:(X-rx)]=0xFFFF0000

rimg[(Y-ry):Y,rx:(X-rx)]=0xFFFF0000

rimg[0:ry,0:rx]=0xFF0000FF

rimg[0:ry,(X-rx):X]=0xFF0000FF

rimg[(Y-ry):Y,0:rx]=0xFF0000FF

rimg[(Y-ry):Y,(X-rx):X]=0xFF0000FF

rimg[0:2, 0:X] = 0xFF000000

rimg[(Y-2):Y, 0:X] = 0xFF000000

for i in range(ny + 1):
    rimg[(ry + y*i):(ry + y*i) + 1, 0:X] = 0xFF000000

rimg[0:Y, 0:2] = 0xFF000000

rimg[0:Y, (X-2):X] = 0xFF000000

for i in range(nx + 1):
    rimg[0:Y, (rx + x*i):(rx + x*i) + 1] = 0xFF000000

img = Image.frombuffer('RGBA',(X,Y),rimg,'raw','RGBA',0,1)

img.show()


from colorama import *

print (Style.BRIGHT)

print (Fore.BLUE + str(x)), 'by', ry, funits

print (Fore.GREEN + str(rx)), 'by', y, funits

print (Fore.RED + str(rx)), 'by', ry, funits

sys.exit()
