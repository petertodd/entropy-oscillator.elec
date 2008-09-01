#!/usr/bin/python

from units import *
from pcb import Pcb
from flipdot import FlipDotModule

array_width = 8
array_height = 13

pitch_x = 71.12 * MM
pitch_y = 10.21 * MM

margin_vert = 1.5 * IN
margin_horz = 1.5 * IN

board_width = (pitch_x * array_width) + (margin_vert * 2)
board_height = (pitch_y * array_height) + (margin_horz * 2)

pcb = Pcb(board_width,board_height)

def mk_line(x1,y1,x2,y2,thick,layer = None):
    # FIXME: what is the 42 for?
    layer.append( \
"""Line[%(x1)d %(y1)d %(x2)d %(y2)d %(thick)d 42 ""]""" \
% {'x1':x1 * 100,
   'y1':y1 * 100,
   'x2':x2 * 100,
   'y2':y2 * 100,
   'thick':thick * 100})

n = 0
for row in range(0,array_width):
    for col in range(0,array_height):
        pcb.elements.append(\
                FlipDotModule((row * pitch_x) + margin_horz,
                              (col * pitch_y) + margin_vert,
                              'F%d' % n))

print '\n'.join(pcb.render())
