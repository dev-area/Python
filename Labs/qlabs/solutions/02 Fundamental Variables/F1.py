#!/usr/bin/python
# Python 2 version

# This race requires 45 laps, how much fuel is required?
FuelPerLap = 2.25   
Laps = 45
FuelRequirement = Laps * FuelPerLap

# Typically a car will carry an extra 50% for contingency 
Fuel = FuelRequirement * 1.5
print "Full fuel load:",Fuel,"kg" 

# The qualifying lap time was 80.45 seconds
# However, that was with only 5kg of fuel
# Each 10 kg of fuel decreases the lap time by 0.35 seconds

QLapTime = 80.45

# Theoretical initial lap time would be
TLapTime = QLapTime - (0.35/10) * 5

print "Theoretical initial lap time:",TLapTime 

LapOneTime = TLapTime + ((Fuel/10) * 0.35)
print "Lap one time:", LapOneTime, "seconds" 



