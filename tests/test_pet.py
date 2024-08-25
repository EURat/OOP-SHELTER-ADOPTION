import pytest
from src.pet import Pet

def test_pet_initialization():
    # Test if a Pet object is initialized correctly
    pet = Pet("Max", 3, "Golden Retriever", "Dog")
    assert pet.name == "Max"
    assert pet.age == 3
    assert pet.breed == "Golden Retriever"
    assert pet.species == "Dog"

def test_pet_str_representation():
    # Test if the __str__ method returns a correct string representation of a Pet object
    pet = Pet("Buddy", 2, "French Bulldog", "Dog")
    expected_str = "Name: Buddy, Age: 2, Breed: French Bulldog, Species: Dog"
    assert str(pet) == expected_str