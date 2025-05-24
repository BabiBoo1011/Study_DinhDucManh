class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, sound):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.sound = sound
    def speak(self):
        print(f"{self.sound} ")
    def display_details(self):
        print(f"The information of {self.name}:")
        print(f"Entry number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught == True:
            print(f"{self.name} has been caught!")
        else:
            print(f"{self.name} has never been caught yet!")

pikachu = Pokemon(1, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True, "Pika Pika")
print("Pikachu! I need you!!!")
pikachu.speak()

pikachu.display_details()