from pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed):
        # Initialize the cat
        super().__init__(name, age)
        self.breed = breed

    # Implement cat-specific methods
    def meow(self):
        print("Meow!")

    def scratch(self):
        print("Scratching...")