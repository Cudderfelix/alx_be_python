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
class Lion(Animal):
    def speak(self):
        return f"{self.name} roars!"
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"   
class Elephant(Animal):
    def speak(self):
        return f"{self.name} trumpets!"     

print(f"{Lion('Simba').speak()}")
print(f"{Dog('Chiwendu').speak()}")
print(f"{Elephant("Dumbo").speak()}")

# Polymorphism Example
