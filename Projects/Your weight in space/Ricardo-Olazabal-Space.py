planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
gravity = [3.7,8.87,9.81,3.711,24.79,10.44,8.69,11.15]
planet = str(input("Select a planet from the list: "+str(planets)+" "))
mass = float(input("Mass on earth (in pounds)="))
w_kg = mass/2.2046
print("Mass in kg: "+str(w_kg))
def calculateweight(mass):
    n_lb = 4.45
    print(f"Your weight on {planets[planets.index(planet)]} is {(w_kg*gravity[planets.index(planet)])/n_lb} lbs.")
calculateweight(mass)
