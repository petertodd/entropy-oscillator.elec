#!/usr/bin/python

"""Make a geda pcb footprint for the 2.7" flip disk strip"""

print """\
Element(%(element_flags)s "%(description)s" "%(pcb_name)s" "%(value)s" %(mark_x)d %(mark_y)d %(text_x)d %(text_y)d %(text_direction)d %(text_scale)d %(text_flags)s)
(""" % \
        { 'element_flags': '0x00',
          'description':'Flip disk strip',
          'pcb_name':'F0',
          'value':'',
          'mark_x':0,
          'mark_y':0,
          'text_x':0,
          'text_y':0,
          'text_direction':0,
          'text_scale':100,
          'text_flags':'0x00',
          }

def put_pin(flags):
    return """\t\
    Pin(%(x)d %(y)d %(thickness)d %(clearance)d %(mask)d %(drillhole)d "%(name)s" "%(number)d" %(flags)s)\
    """ % flags 

for i in range(0,14):
    print put_pin(\
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

print ")"
