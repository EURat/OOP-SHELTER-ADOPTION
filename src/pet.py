class Pet:
    def __init__(self, name, age, breed, species):
        # Initialize the pet attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.species = species

    # Implement other necessary methods
    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def sound(self):
        # This method can be overridden by child classes to make specific sounds
        pass

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed} {self.species}."