from units import *
from collections import deque

class Pin:
    def __init__(self,
            x = 0,
            y = 0,
            thickness = 0,
            clearance = 0,
            mask = 0,
            drillhole = 0,
            name = '',
            number = 0,
            flags = '0x00'):
        self.x = x
        self.y = y
        self.thickness = thickness
        self.clearance = clearance
        self.mask = mask
        self.drillhole = drillhole
        self.name = name
        self.number = number
        self.flags = flags

    def render(self):
        return """\
Pin(%(x)d %(y)d %(thickness)d %(clearance)d %(mask)d %(drillhole)d "%(name)s" "%(number)d" %(flags)s)""" % \
            { 'x':self.x / MIL,
              'y':self.y / MIL,
              'thickness':self.thickness / MIL,
              'clearance':self.clearance / MIL,
              'mask':self.mask / MIL,
              'drillhole':self.drillhole / MIL,
              'name':self.name,
              'number':self.number,
              'flags':self.flags,}

class Element:
    def __init__(self,
        element_flags = '0x00',
        description = '',
        pcb_name = None,
        value = '',
        mark_x = 0,
        mark_y = 0,
        text_x = 0,
        text_y = 0,
        text_direction = 0,
        text_scale = 100,
        text_flags = '0x00'):

        self.element_flags = element_flags
        self.description = description
        self.pcb_name = pcb_name
        self.value = value
        self.mark_x = mark_x
        self.mark_y = mark_y
        self.text_x = text_x
        self.text_y = text_y
        self.text_direction = text_direction
        self.text_scale = text_scale
        self.text_flags = text_flags

        self.pins = []

    def render(self):
        r = deque()

        r.append("""\
Element(%(element_flags)s "%(description)s" "%(pcb_name)s" "%(value)s" %(mark_x)d %(mark_y)d %(text_x)d %(text_y)d %(text_direction)d %(text_scale)d %(text_flags)s)
    (""" % \
            { 'element_flags': self.element_flags,
              'description':self.description,
              'pcb_name':self.pcb_name,
              'value':self.value,
              'mark_x':self.mark_x / MIL,
              'mark_y':self.mark_y / MIL,
              'text_x':self.text_x / MIL,
              'text_y':self.text_y / MIL,
              'text_direction':self.text_direction,
              'text_scale':self.text_scale,
              'text_flags':self.text_flags,
              })

        for p in self.pins:
            r.append(p.render())

        r.append(')')
        return r
