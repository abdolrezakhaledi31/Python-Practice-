squares =[x**3 for x in range(1, 6)]
print(squares)
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
events = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for x in range(events):
    if x % 2 == 0:
        print(x)