from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed):
        # Initialize the dog
        super().__init__(name, age)
        self.breed = breed

    # Implement dog-specific methods
    def bark(self):
        print("Woof!")

    def wag_tail(self):
        print("Wagging tail...")