from shelter import Shelter
from dog import Dog
from cat import Cat

def main():
    shelter = Shelter()

    while True:
        print("\n=== Pet Adoption System ===")
        print("1. List all pets")
        print("2. Add a new pet")
        print("3. Search for a pet")
        print("4. Adopt a pet")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Implement list all pets
            shelter.list_pets()
        elif choice == '2':
            # Implement add new pet
            name = input("Enter pet name: ")
            age = input("Enter pet age: ")
            breed = input("Enter pet breed: ")
            species = input("Enter pet species: ")
            pet = Pet(name, age, breed, species)
            shelter.add_pet(pet)
        elif choice == '3':
            # Implement search for a pet
            name = input("Enter pet name to search: ")
            pet = shelter.search_pet(name)
            if pet:
                print(pet)
            else:
                print("Pet not found")
        elif choice == '4':
            # Implement adopt a pet
            name = input("Enter pet name to adopt: ")
            shelter.adopt_pet(name)
        elif choice == '5':
            print("Thank you for using the Pet Adoption System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()