# Question 1 list
numbers = [5, 3, 8, 2, 23]
print(max(numbers))

# Question 2 dictionary
my_info = {"name": "Jmaro", "age": 49, "city": "Matrix"}
for key, value in my_info.items():
    print(key, value)
# Question 3 changing list to a set
num = [1, 1, 2, 5, 4, 4]
num1 = set(num)
print(num)
print(num1)
print(len(num1))
# Question 4
coords = (1, 2, 5)
x, y, z = coords
print(x)
print(y)
print(z)
print(coords[0])
print(coords[1])
print(coords[2])
coords[1] = 6
