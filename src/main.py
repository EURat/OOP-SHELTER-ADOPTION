from shelter import Shelter

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
            # TODO: Implement list all pets
        elif choice == '2':
            # TODO: Implement add new pet
        elif choice == '3':
            # TODO: Implement search for a pet
        elif choice == '4':
            # TODO: Implement adopt a pet
        elif choice == '5':
            print("Thank you for using the Pet Adoption System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()