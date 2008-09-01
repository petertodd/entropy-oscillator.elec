from units import *

from collections import deque

class Pcb:
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.solder = deque()
        self.component = deque()

        self.layers = \
                 (('1 "solder"',self.solder),
                  ('2 "GND-sldr"',deque()),
                  ('3 "Vcc-sldr"',deque()),
                  ('4 "component"',self.component),
                  ('5 "GND-comp"',deque()),
                  ('6 "Vcc-comp"',deque()),
                  ('7 "unused"',deque()),
                  ('8 "unused"',deque()))

    def render(self):
        r = deque()
        r.append(\
"""PCB["" %(board_width)d %(board_height)d]

Grid[2500.000000 0 0 1]
Cursor[0 272500 6.000000]
Thermal[0.500000]
DRC[1000 1000 1000 1000 1500 1000]
Flags(0x00000000000010d8)
Groups("1,2,3,s:4,5,6,c:s:c")
Styles["Signal,1500,4000,2000,1000:Power,2500,6000,3500,1000:Fat,4000,6000,3500,1000
:Skinny,800,3600,2000,1000"]""" \
    % {'board_width':self.width / CMIL,
       'board_height':self.height / CMIL})

        for (n,v) in self.layers:
            r.append('Layer(%s)' % n)
            r.append('(')
            r.append('\n'.join(['\t' + c for c in v]))
            r.append(')')

        return r
