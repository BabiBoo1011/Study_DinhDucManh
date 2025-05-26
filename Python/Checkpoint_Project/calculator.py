import math
def triangle(base, height):
    return 0.5 * base * height
def rectangle(length, width):
    return length * width
def square(side):
    return side * side
def circle(radius):
    return math.pi * radius * radius
print("==================")
print("Welcome to the Calculator!")
print("==================")
print("\n")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")

option = int(input("Which shape: "))

if option == 1:
    base = float(input("Base: "))
    height = float(input("Height: "))
    print("\nArea of triangle is: ", triangle(base, height))
elif option == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    print("\nArea of rectangle is: ", rectangle(length, width))
elif option == 3:
    side = float(input("Side: "))
    print("\nArea of square is: ", square(side))
elif option == 4:
    radius = float(input("Radius: "))
    print("\nArea of circle is: ", circle(radius))
elif option == 5:
    print("\nGoodbye! See you next time!")