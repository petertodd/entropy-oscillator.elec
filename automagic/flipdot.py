from units import *
from element import Element,Pin

class FlipDotModule(Element):
    def __init__(self,
            mark_x,
            mark_y,
            pcb_name):
        Element.__init__(self,mark_x = mark_x,mark_y = mark_y,
                         pcb_name = pcb_name)

        num_dots = 7
        dot_pitch_x = 10.16 * MM

        cathode_offset_x = 7 * MM
        cathode_offset_y = 3.2 * MM

        class Dot:
            def __init__(self,x,y,i):
                d = {'thickness':1.3 * MM,
                     'clearance':0.1 * MM,
                     'mask':0.1 * MM,
                     'drillhole':1 * MM} # FIXME: check this!

                self.anode = Pin(x = x,y = y,
                                 number = i * 2 + 1,
                                 **d)
                self.cathode = Pin(x = x + cathode_offset_x,
                                   y = y + cathode_offset_y,
                                   number = i * 2 + 2,
                                   **d)

        self.dot = []
        x = 0
        for i in range(0,7):
            self.dot.append(Dot(x,0,i))
            x += dot_pitch_x
            self.pins.append(self.dot[i].anode)
            self.pins.append(self.dot[i].cathode)
