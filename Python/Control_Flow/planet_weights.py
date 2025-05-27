print("Here is the planet number: ")
print("1\tMercury")
print("2\tVenus")
print("3\tMars")
print("4\tJupiter")
print("5\tSaturn")
print("6\tUranus")
print("7\tNeptune")

w = float(input("Please enter your Earth weight: "))
p = int(input("Please enter the planet number: "))
g = 0.0
if p == 1:
    g = 0.38
elif p == 2:
    g = 0.91
elif p == 3:
    g = 0.38
elif p == 4:
    g = 2.53
elif p == 5:
    g = 1.07
elif p == 6:
    g = 0.89
elif p == 7:
    g = 1.14
w = w * g
print(f"Your weight on the destination planet is: {w}")
