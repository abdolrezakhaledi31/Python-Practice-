while True:
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number:"))
        result = number1 / number2
        
    except ValueError:
        print("Input jast whole number")
    except ZeroDivisionError:
        print("Number cant be Zero")
    else:
        print(result)
        break