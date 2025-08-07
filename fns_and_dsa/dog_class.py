class Dog:
    def __init__(self, name, fur_length, height):
        self.name = name
        self.fur_length = fur_length
        self.height = height
    
    def barking_sound(self, barking_sound):
        return barking_sound
    def speed(self, speed):
        return speed

# Objection Creation
dog1 = Dog("Chiwendu", "short", "medium")
dog2 = Dog ("Musa", "long", "tall")
dog3 = Dog ("Abacha", "medium", "short")

print(f"{dog1.name} has a {dog1.fur_length} fur and {dog1.height} height. with a barking sound of {dog1.barking_sound("lala!")} and speed of {dog1.speed("30km/h")}.")

# Real World Example #Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def color(self):
        pass
class Lion(Animal):
    def speak(self):
        return f"{self.name} roars!"
    def color(self):
        return f"{self.name} is brown in color."
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"
    def color(self):
        return f"{self.name} is white in color."
class Elephant(Animal):
    def speak(self):
        return f"{self.name} trumpets!"
    def color(self):
        return f"{self.name} is grey in color." 
class Tiger(Animal):
    def speak(self):
        return f"{self.name} growls!"
    def color(self):
        return f"{self.name} is stripped yellow and black in color."    

print(f"{Lion('Simba').speak()}")
print(f"{Dog('Chiwendu').speak()}")
print(f"{Elephant("Dumbo").speak()}")
print(f"{Tiger('Sher Khan').speak()}")

# Polymorphism Example
zoo_animals = [
    Lion("Simba"),
    Elephant("Dumbo"),
    Dog("Chinwendu"),
    Tiger("Sher Khan")
]
for animal in zoo_animals:
   print(animal.speak(), animal.color())