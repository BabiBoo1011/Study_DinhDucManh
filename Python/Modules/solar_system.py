from math import pi
from random import choice as ch
def surface_area(r):
    return 4 * pi * (r ** 2)
planets = ['Mercury', 'Venus', 'Earth', 'Mars','Saturn']
def calculate_planet_surface_area():
    random_planet = ch(planets)
    if random_planet == 'Mercury':
        r = 2440
        print(f"{random_planet}'s surface area is {surface_area(r)}")
    elif random_planet == 'Venus':
        r = 6052
        print(f"{random_planet}'s surface area is {surface_area(r)}")
    elif random_planet == 'Earth':
        r = 6371
        print(f"{random_planet}'s surface area is {surface_area(r)}")
    elif random_planet == 'Mars':
        r = 3390
        print(f"{random_planet}'s surface area is {surface_area(r)}")
    elif random_planet == 'Saturn':
        r = 58232
        print(f"{random_planet}'s surface area is {surface_area(r)}")
    else:
        print("Oops! An error occurred.")

for i in range (10):
  calculate_planet_surface_area()