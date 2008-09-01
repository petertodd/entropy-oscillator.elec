"""Conversion constants.

Usage:

Converting from inches to meters:

x = 10 * IN

Converting to inches from meters:

y = x / IN
"""

# Meters are the native unit
M = 1

# Other metric units
CM = M * 1e-2
MM = CM * 1e-1

# Imperial
IN = 25.4 * MM

# These two are used by geda, mils and centi-mils
MIL = IN * 1e-3
CMIL = MIL * 1e-2
