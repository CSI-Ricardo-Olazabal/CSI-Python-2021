import math
name = "FN GL40"
calibre = "40x46 mm"
ammo = "M441(HE) grenade"
pspeed = 249.344
height = 1776
def CalculateDistanceTime():
    time = math.sqrt((2*height)/(32.1522))
    distance = pspeed*time
    print(f"Time: {time} seconds.")
    print(f"Distance: {distance} feet.")
    print(f"Given the speed of the projectile ({pspeed} feet/second) and the height of the building ({height} feet), \nwe can calculate the time: {time} seconds, and now, using the time and speed, \nwe can calculate distance: {distance} feet.")
CalculateDistanceTime()