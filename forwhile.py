# for i in range(5):
#     print(i)
# 
# for i in range(2, 6):
#     print(i)
# 
# for i in range(0, 12, 4):
#     print(i)
# 
# names = ["sara", "ali", "reza"]
# for name in names:
#     print(name)
# 
# for index, color in enumerate(["green", "blue", "red"]):
#     print(index, color)

# total = 0
# for i in range(1, 101):
#     total = total + i
#     
# print(total)
# 
# fruits = ["apple", "banana", "orange", "avocado", "mushroom"]
# for index, fruit in enumerate(fruits):
#     print(f"The fruit number{index +1} is {fruit}")
    
    
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()
