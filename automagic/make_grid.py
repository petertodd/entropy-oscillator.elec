#!/usr/bin/python


array_width = 8
array_height = 13

pitch_x = 2800
pitch_y = 402

margin_vert = 1000
margin_horz = 1000

board_width = (pitch_x * array_width) + (margin_vert * 2)
board_height = (pitch_y * array_height) + (margin_horz * 2)

fpcb = open('grid.pcb','w')


def mk_flip_disk(x,y,name):
    """Make a geda pcb footprint for the 2.7" flip disk strip"""

    print >>fpcb,"""\
    Element(%(element_flags)s "%(description)s" "%(pcb_name)s" "%(value)s" %(mark_x)d %(mark_y)d %(text_x)d %(text_y)d %(text_direction)d %(text_scale)d %(text_flags)s)
    (""" % \
            { 'element_flags': '0x00',
              'description':'Flip disk strip',
              'pcb_name':name,
              'value':'',
              'mark_x':x,
              'mark_y':y,
              'text_x':50,
              'text_y':50,
              'text_direction':0,
              'text_scale':100,
              'text_flags':'0x00',
              }

    def put_pin(flags):
        return """\t\
        Pin(%(x)d %(y)d %(thickness)d %(clearance)d %(mask)d %(drillhole)d "%(name)s" "%(number)d" %(flags)s)\
        """ % flags 

    for i in range(0,14):
        print >>fpcb,put_pin(\
                 { 'x': ((i / 2) * 400) + (126 * (i % 2)),
                  'y': 275 * (i % 2),
                  'thickness': 72,
                  'clearance': 10,
                  'mask': 10,
                  'drillhole': 52,
                  'name': str(i + 1),
                  'number': i + 1,
                  'flags': '0x00',
                  })

    print >>fpcb,")"

print >>fpcb,\
"""PCB("" %(board_width)d %(board_height)d)

Grid[2500.000000 0 0 1]
Cursor[0 272500 6.000000]
Thermal[0.500000]
DRC[1000 1000 1000 1000 1500 1000]
Flags(0x00000000000010d8)
Groups("1,2,3,s:4,5,6,c:s:c")
Styles["Signal,1500,4000,2000,1000:Power,2500,6000,3500,1000:Fat,4000,6000,3500,1000:Skinny,800,3600,2000,1000"]
""" % {'board_width':board_width,
       'board_height':board_height}

n = 0
for row in range(0,array_width):
    for col in range(0,array_height):
        n = n + 1
        mk_flip_disk((row * pitch_x) + margin_horz,
                     (col * pitch_y) + margin_vert,
                     'F%d' % n)
