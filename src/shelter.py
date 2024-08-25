class Shelter:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        # Implement method to add a pet to the shelter
        if isinstance(pet, Pet):
            self.pets.append(pet)
            print(f"{pet.name} has been added to the shelter.")
        else:
            print("Only Pet instances can be added to the shelter.")

    def list_pets(self):
        # Implement method to list all pets in the shelter
        if self.pets:
            print("Pets in the shelter:")
            for pet in self.pets:
                print(pet)
        else:
            print("The shelter is empty.")

    def search_pet(self, name):
        # Implement method to search for a pet by name
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None

    def adopt_pet(self, name):
        # Implement method to adopt a pet by name
        pet = self.search_pet(name)
        if pet:
            self.pets.remove(pet)
            print(f"{pet.name} has been adopted.")
            return pet
        else:
            print(f"No pet found with the name {name}.")