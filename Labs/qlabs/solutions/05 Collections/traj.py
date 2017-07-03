# Python 2 version
# Calculate the height of a projectile
# (Ignores air resistance)
from math import pi, tan, cos

# 1 Mile per Hour = 0.44704 Meters per Second 

g     = 9.81          # Acceleration due to gravity m/s squared
v0    = 44            # The initial velocity m/s
theta = 80 * pi/180   # elevation angle in radians
x     = 0.5           # the horizontal distance travelled
y0    = 1             # height of the barrel (m)

# Initial values for the graphic
y = y0
x = 0.0
x_axis = []
y_axis = []

while y > 0:
    x = x + 0.1
    y = y0 + x*tan(theta) - (g*x**2)/(2*((v0*cos(theta))**2))
 
    print 'x = %.1f m, y     = %.1f m' % (x,y) 
    x_axis.append(x)
    y_axis.append(y)

# Graph
import matplotlib.pyplot as pyplot

pyplot.ylabel('Height m')
pyplot.xlabel('Distance m')

pyplot.ylim(-1,max(max(x_axis),max(y_axis)))       # Optional realism

pyplot.plot(x_axis, y_axis)
pyplot.show()


