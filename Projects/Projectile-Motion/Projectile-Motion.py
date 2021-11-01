import math
def ProjectileFunction(gun:str,caliber:str,ammo:str,pspeed:int,height:int,building:str,gravity:int):
    time = math.sqrt((2*height)/gravity)
    distance = pspeed*time
    print(f"The gun selected for this experiment was a(n) {gun} with ammo {ammo}. The caliber is {caliber}.")
    print(f"Time: {time} seconds.")
    print(f"Distance: {distance} feet.")
    print(f"Given the speed of the projectile ({pspeed} feet/second) and the height of the {building} ({height} feet), \nwe can calculate the time: {time} seconds, and now, using the time and speed, \nwe can calculate distance: {distance} feet.")
ProjectileFunction("FN GL40","40x46 mm","M441(HE) grenade",76,541,"One World Trade Center",10)
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