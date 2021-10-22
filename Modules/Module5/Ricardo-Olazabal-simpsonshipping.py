from typing import get_type_hints


print("Simpson shipping.")
weight = float(input("What is the weight of the package? \n"))
g = 0.00
c = 0.00
d = 0.00
if (weight <= 2):
    g = 1.75+20
    c = 3.50+20
    d = 5.25
else:
    if (weight <= 6):
        g = 3.50+20
        c = 7+8
        d = 10.50
    else:
        if (weight <= 10):
            g = 4.50+20
            c = 9+12
            d = 13.50
        else:
            g = 5.25+20
            c = 10.50+15
            d = 15.75
print(f"Ground shipping: ${weight*g}.")
print(f"Courier shipping: ${weight*c}.")
print(f"Drone shipping: ${weight*d}.")
print(f"Premium ground shipping: $150.")