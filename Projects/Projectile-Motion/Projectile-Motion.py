import math
def ProjectileFunction(experimentalData: experimentalData):
    time = math.sqrt((2*experimentalData.height)/experimentalData.gravity)
    distance = experimentalData.pspeed*time
    print(f"The gun selected for this experiment was a(n) {experimentalData.gun} with ammo {experimentalData.ammo}. The caliber is {experimentalData.caliber}.")
    print(f"Time: {time} seconds.")
    print(f"Distance: {distance} feet.")
    print(f"Given the speed of the projectile ({experimentalData.pspeed} feet/second) and the height of the {experimentalData.building} ({experimentalData.height} feet), \nwe can calculate the time: {experimentalData.time} seconds, and now, using the time and speed, \nwe can calculate distance: {experimentalData.distance} feet.")
#ProjectileFunction("FN GL40","40x46 mm","M441(HE) grenade",76,541,"One World Trade Center",10)

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