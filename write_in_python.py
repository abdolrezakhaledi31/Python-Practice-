with open("test.txt", "a", encoding="utf-8")as file:
    file.write("goodbye\n")
    
    
with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")