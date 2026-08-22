try:
    note = input("Enter the name of your file: ")
    with open(note, "r", encoding="utf-8") as file:
        contect = file.read()
except FileNotFoundError:
    print("Wrong name.Enter correct name.")
else:
    print(contect)
    