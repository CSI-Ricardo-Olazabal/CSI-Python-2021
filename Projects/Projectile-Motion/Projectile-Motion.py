import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
def projectileFunction(experimentalData: ExperimentalData):
    planet = experimentalData.planet
    time = math.sqrt((2*experimentalData.height)/(g_ms2[planets.index(planet)]*3.28084))
    distance = experimentalData.pspeed*time
    print(f"The gun selected for this experiment was a(n) {experimentalData.gun} with ammo {experimentalData.ammo}. The caliber is {experimentalData.caliber}.")
    print(f"Time: {time} seconds.")
    print(f"Distance: {distance} feet.")
    print(f"Given the speed of the projectile ({experimentalData.pspeed} feet/second), the force of gravity on {planet} ({g_ms2[planets.index(planet)]*3.28084} ft/s^2) and, the height of the {experimentalData.building} ({experimentalData.height} feet), \nwe can calculate the time to be {time} seconds, and now, using the time and speed, \nwe can calculate distance to be {distance} feet.")
#experimentalData = ExperimentalData("FN GL40","40x46 mm","M441(HE) grenade",76,541,"One World Trade Center",10)
myDataSet = [
ExperimentalData("FN GL40","40x46 mm","M441(HE) grenade",76,541,"One World Trade Center","Earth"),
ExperimentalData("FN GL40","40x46 mm","M441(HE) grenade",76,830,"Burj Khalifa","Venus"),
ExperimentalData("FN GL40","40x46 mm","M576 (MP-APERS) grenade",269,541,"One World Trade Center","Mars"),
ExperimentalData("FN GL40","40x46 mm","M576 (MP-APERS) grenade",269,830,"Burj Khalifa","Jupiter"),
ExperimentalData("NSV \"Utes\"","12.7x108mm","mm BZT-44M gzh",818,830,"Burj Khalifa","Neptune")
]
for data in myDataSet:
    print("\n-----------------------------------------------------------\n")
    projectileFunction(data)

#serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')
print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
#name = "FN GL40"
#calibur = "40x46 mm"
#ammo = "M441(HE) grenade"
#pspeed = 249.344
#height = 1776
#def CalculateDistanceTime():
#    time = math.sqrt((2*height)/(32.1522))
#    distance = pspeed*time
#    print(f"Time: {time} seconds.")
#    print(f"Distance: {distance} feet.")
#    print(f"Given the speed of the projectile ({pspeed} feet/second) and the height of the building ({height} feet), \nwe can calculate the time: {time} seconds, and now, using the time and speed, \nwe can calculate distance: {distance} feet.")
#CalculateDistanceTime()