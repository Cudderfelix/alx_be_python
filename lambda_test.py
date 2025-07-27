add = lambda x, y: x + y
result = add(5, 3)
print(result) #Output: 8

count = 0
def increment_global():
    global count 
    count += 1
increment_global()
print(count) #output: 1 (Global count is modified)

def outer_function():
    x = 10 #Variable in the enclosing function

    def inner_function():
        nonlocal x #Using nonlocal to modify x from the enclosing function
        x += 5 #Modifying the value of x

        inner_function() # Calling the nested function
        print("Modified value of x from inner function:", x)
outer_function()


def greet():
    print("Hello, how are you doing my friend")
greet() #Output: Hello, how are you doing my friend
print(greet)