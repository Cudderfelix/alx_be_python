add = lambda x, y: x + y
result = add(5, 3)
print(result) #Output: 8

count = 0
def increment_global():
    global count 
    count += 1
increment_global()
print(count) #output: 1 (Global count is modified)