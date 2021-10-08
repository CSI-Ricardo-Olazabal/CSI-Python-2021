print("Jumping on other planets")
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
rel_grav = [2.65,1.11,1,2.64,0.40,0.94,1.13,0.88]
planet = str(input("Select a planet from the list: "+str(planets)+" "))
jump = (float(input("What is your jump's length on Earth in inches?= ")))*0.0254
jump2 = jump*rel_grav[planets.index(planet)]
print(f"Your jump on Earth is {jump} meters.")
print(f"Your jump on {planets[planets.index(planet)]} is {jump2} meters.")