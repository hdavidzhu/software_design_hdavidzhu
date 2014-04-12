"""
Created 20140127
David Zhu
"""
# print "Hello world!"

import unum
from unum import Unum
from unum.units import *

# speed = 90*mile/h
# print speed.asUnit(m/s)

# Suppose you are tightening the lug nuts on a 2004 Honda Pilot.  The manual calls for 181 foot-pounds of torque, but your torque wrench is in SI units.  Convert to Newton-meters.  Hint: define ft in terms of m and lb in terms of kg, and don't forget that there are two kinds of "pounds".

# ft = Unum.unit('foot',mile/5280.0)
# lbf = Unum.unit('lbf',4.4482216*N)

# torque = 181*ft*lbf
# print torque.asUnit(N*M)

# What are the units of a watt-volt-farad-ohm-siemens per coulomb-Hertz-Joule?

print 1*W*V*F*ohm*S/(C*Hz*J)