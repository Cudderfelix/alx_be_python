class student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
student1 = student("Chinwendu", "20")
student2 = student("Musa", 22)
student3 = student("Abacha", 21)
print(f"{student1.name} is {student1.age} years old. \n {student2.name} is {student2.age} years old. \n {student3.name} is {student3.age} years old.")


# Creating a product catalogue

class product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def stock_value(self):
        return self.price * self.quantity
