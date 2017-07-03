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

y = y0 + x*tan(theta) - (g*x**2)/(2*((v0*cos(theta))**2))

print 'Height:',y,'m' 