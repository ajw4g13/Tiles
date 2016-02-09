

    ### This code uses inputted dimensions for a rectangular room and a
    ### rectangular tile, and outputs the number of tiles needed to tile the
    ### room optimally. It then outputs instructions on how to tile your room,
    ### a diagram of the final room, the number of tiles needed etc...


## This section takes inputted x and y dimensions for the room and tile and
## gives the x and y dimensions in millimetres.

import sys

allowed_units = ['metre', 'metres', 'm', 1000.0, 'centimetre', 'centimetres', 'cm', 10.0, 'milimetre', 'milimetres', 'mm', 1.0, 'yard', 'yards', 'yd', 914.4, 'foot', 'feet', 'ft', 304.8, 'inch', 'inches', 'in', 25.4]

ilx, ily, tunits = float(input("Width of tile: ")), float(input("Length of tile: ")), raw_input("type units: ")
                                          # ilx and ily is the inputted width 
                                          # and height of the tiles, with units
                                          # tunits.

lx, ly, Lx, Ly = 0, 0, 0, 0

for i in range(len(allowed_units)/4):
    if tunits == allowed_units[4*i] or tunits == allowed_units[4*i + 1] or tunits == allowed_units[4*i + 2]:
        lx, ly = allowed_units[4*i + 3] * ilx, allowed_units[4*i + 3] * ily

                                          # This code assigns the units that
                                          # final tile measurements are given
                                          # in, based on inputted tile units, 
                                          # while simultaneously defining new
                                          # values for the length and width of
                                          # the tile, lx and ly, in millimetres.

if lx == 0 or ly == 0:
    sys.exit('Invalid dimensions or units entered.')

iLx, iLy, runits = float(input("Width of room: ")), float(input("Length of room: ")), raw_input("type units: ")

for i in range(6):
    if runits == allowed_units[4*i] or runits == allowed_units[4*i + 1] or runits == allowed_units[4*i + 2]:
        Lx, Ly = allowed_units[4*i + 3] * iLx, allowed_units[4*i + 3] * iLy                                                                           

                                          # Repeat of above, for room.

if Lx == 0 or Ly == 0:
    sys.exit('Invalid dimensions or units entered.')


## This section takes the x and y dimensions in millimetres, and gives the
## number of tiles needed in both directions, along with the total number of
## tiles needed, for both alignments. It then gives the dimensions for the
## side tiles, in millimetres.

nxa = int(Lx / lx - 1.0)
nya = int(Ly / ly - 1.0)                  # Number of tiles needed in x and y
                                          # directions.

Na = (nxa + 2) * (nya + 2)                # Total number of tiles needed.

nxb = int(Lx / ly - 1.0)
nyb = int(Ly / lx - 1.0)
    
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

Rx = 0.5*(Lx-(nx*lx))

Ry = 0.5*(Ly-(ny*ly))
                                          # Remainder of tiles in millimetres
                                          # (float).

print (" ")    


## This section uses the inputted x and y dimensions for the room and tile
## to give an image of the tiled room.

from PIL import Image

import numpy as np

X, Y, x, y, rx, ry = int(round(Lx)), int(round(Ly)), int(round(lx)), int(round(ly)), int(round(Rx)), int(round(Ry))
                                          # Returns integer values for all the
                                          # lengths in previous section, in  
                                          # order to assign pixels.

rimg = np.empty((X,Y),np.uint32)          # Uses the room dimensions to create
                                          # an empty array, to be used for the
                                          # room image.

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
                                          # Creates coloured tiles around edges
                                          # of the image.


rimg[0:9, 0:X] = 0xFF000000

rimg[(Y-9):Y, 0:X] = 0xFF000000

rimg[0:Y, 0:9] = 0xFF000000

rimg[0:Y, (X-9):X] = 0xFF000000
                                          # Creates a black border around the 
                                          # image.

for i in range(ny + 1):
    rimg[((ry + y*i) - 4):((ry + y*i) + 5), 0:X] = 0xFF000000

for i in range(nx + 1):
    rimg[0:Y, (rx + x*i):(rx + x*i) + 1] = 0xFF000000
                                          # Creates black lines at intervals,
                                          # representing the tiles.

img = Image.frombuffer('RGBA',(X,Y),rimg,'raw','RGBA',0,1)

img.save("room_layout.png","PNG")

img.show()

print N, 'tiles needed'

print ' '

print 'The side tiles (green) will be', ilx*(Rx/lx), tunits, 'by', ily, tunits

print 'The side tiles (blue) will be', ilx, tunits, 'by', ily*(Ry/ly), tunits

print 'The corner tiles (red) will be', ilx*(Rx/lx), tunits, 'by', ily*(Ry/ly), tunits, '.'

print ' '

if (nx % 2 != 0) and (ny % 2 != 0):
    print "In order to lay your floor, mark the centre point of the room. Place a tile so that it's centre lines up with the centre of the centre of the room. Then place your tiles so that they all line up with this central tile." 
elif (nx % 2 == 0) and (ny % 2 == 0):
    print "In order to lay your floor, mark the centre point of the room. Place four tiles so that each has a corner on the centre point of the room. Then place your tiles so that they all line up with these central tiles." 
elif (nx % 2 != 0) and (ny % 2 == 0) and Lx < Ly:
    print "In order to lay your floor, mark the centre point of the room. Place a tile either side of the point so that the tiles line up with the long side of the room. Then place your tiles so that they all line up with this central tile." 
elif (nx % 2 == 0) and (ny % 2 != 0) and Lx > Ly:
    print "In order to lay your floor, mark the centre point of the room. Place a tile either side of the point so that the tiles line up with the long side of the room. Then place your tiles so that they all line up with this central tile." 
elif (nx % 2 != 0) and (ny % 2 == 0) and Lx > Ly:
    print "In order to lay your floor, mark the centre point of the room. Place a tile either side of the point so that the tiles line up with the short side of the room. Then place your tiles so that they all line up with this central tile." 
elif (nx % 2 == 0) and (ny % 2 != 0) and Lx < Ly:
    print "In order to lay your floor, mark the centre point of the room. Place a tile either side of the point so that the tiles line up with the short side of the room. Then place your tiles so that they all line up with this central tile." 

raw_input("press enter to exit")
