#!/usr/bin/python

# This race requires 45 laps, how much fuel is required?
FuelPerLap = 2.25   
Laps = 45
FuelRequirement = Laps * FuelPerLap

# Typically a car will carry an extra 50% for contingency 
Fuel = FuelRequirement * 1.5
print("Full fuel load:",Fuel,"kg")

# The qualifying lap time was 80.45 seconds
# However, that was with only 5kg of fuel
# Each 10 kg of fuel decreases the lap time by 0.35 seconds

QLapTime = 80.45

# Theoretical initial lap time would be
TLapTime = QLapTime - (0.35/10) * 5

Lap = 1
TyreLap = 1
LapTimes = []

while Lap <= Laps:
    Fuel = Fuel - FuelPerLap
    LapTime = TLapTime + ((Fuel/10) * 0.35)
    
    if Lap == 20:
        print("New tyres")
        TyreLap = 1
    else:
        LapTime = LapTime + (0.05 * TyreLap)  

    print("Lap",Lap,"time:", LapTime, "seconds")
    LapTimes.append(LapTime)
    Lap = Lap + 1
    TyreLap = TyreLap + 1


# Graph
import matplotlib.pyplot as plot

x_axis = range(1,Laps+1)
plot.ylabel('Lap time (seconds)')
plot.xlabel('Lap number')

plot.plot(x_axis, LapTimes)
plot.show()



