import random
symbols = ["cherry", "grape", "watermelon", "seven"]

def play():
    result = random.choices(symbols, k = 3)
    print(f"Result: {result}")
    if result[0] == result[1] and result[1] == result[2] and result[2] == "seven":
        print("Jackpot!")
    else:
        print("Thanks for playing!")

while True:
    choice = int(input("You wanna play? Please choose 1 (Yes) or 0 (No): "))
    if choice == 1:
        play()
    if choice == 0:
        print("Goodbye")
        break
    if choice != 1 and choice != 0:
        print("Please choose 1 (Yes) or 0 (No): ")