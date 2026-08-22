class ItemNotFoundError(Exception):
    pass
class InsufficientStockError(Exception):
    pass

inventory = {"apple": 10, "banana": 5, "orange": 0}

while True:
    item = input("Enter item name (or type 'exit' to quit): ")
    if item == "exit":
        break
    try:
        if item in inventory:
            count = int(input("Enter quantity: "))
            if count > inventory[item]:
                raise InsufficientStockError("Requested amount exceeds stock.")
        else:
            raise ItemNotFoundError("Item not found.")

    except ItemNotFoundError as e:
        print("Item not found: ", e)
    except InsufficientStockError as e:
        print("Not enough stock: ", e)
    except ValueError:
        print("Please enter a valid number.")
    else:
        inventory[item] -= count
        print("It's done")
        
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"{item}:{count} sold\n")
            
with open("log.txt", "r", encoding="utf-8") as file:
    info = file.read()
    print(info)