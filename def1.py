# Create a function called greet_user.
# It should:
# accept one parameter called name
# print:
def greet_user(name):
    print(name)
greet_user("jouny")
    

# Create a function called double.
# It should:
# accept one number
# return that number multiplied by 2
# Example:
def double (number):
    return number * 2
result = double(5)

print(result)



# Create a function called is_even.
# It should:
# accept one number
# return True if the number is even
# return False if the number is odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4))
print(is_even(7))

# Create a function called get_full_name.
# It should:
# accept first_name and last_name
# return the full name as one string
def get_full(first_name, last_name):
    return first_name + last_name
full_name = get_full("Jon", "DJ")

print(full_name)

# Create a function called countdown.
# It should:
# accept a number n
# print numbers from n down to 1
def countdown(n):
    for i in range(5, 0, -1):
        print(i)
countdown(5)

def multiply_all(*args):
    result = 1
    for num in args:
        result = result * num
    return result

answer = multiply_all(2, 3, 4)
print(answer)

#تابعی به اسم square بنویس که یه عدد می‌گیره و مربعش رو return می‌کنه.
def square(num):
    return num * num

print(square(5))

#تابعی به اسم is_even بنویس که یه عدد می‌گیره و True/False برمی‌گردونه (زوج بودن).
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(5))
print(is_even(8))

#تابعی به اسم greet بنویس که اسم رو می‌گیره و پیام خوش‌آمدگویی رو return می‌کنه (نه print).
def greet(name):
    return name + " خوش آمديد"
print(greet("علي"))

#تابعی به اسم power بنویس با دو پارامتر base و exponent، که exponent مقدار پیش‌فرض ۲ داشته باشه (یعنی اگه نفرستیم، مربع حساب کنه
def power(base, exponent = 2):
    return base ** exponent
print(power(4))
print(power(2, 3))

#تابعی به اسم make_coffee بنویس با پارامتر size که پیش‌فرضش "medium" باشه و یه جمله برگردونه مثل: "یه قهوه‌ی medium لطفاً".
def make_coffee(size = "medium"):
    return f"يک قهوه {size} لطفا"

print(make_coffee())
print(make_coffee("larg"))

#تابعی به اسم min_max بنویس که یه لیست از اعداد می‌گیره و کوچیک‌ترین و بزرگ‌ترین رو با هم (به‌شکل tuple) return می‌کنه.
def min_max(numbers):
    return min(numbers), max(numbers)
nums = [5, 2, 7, 1]

print(min_max(nums))

#تابعی به اسم divide بنویس که دو عدد می‌گیره و هم خارج‌قسمت هم باقیمانده رو با هم برمی‌گردونه.
def divide(num1, num2):
    quotient = num1 // num2
    reminder = num1 % num2
    return quotient, reminder
result = divide(18, 6)

print(result)

#تابعی به اسم get_age بنویس که با input() سن رو از کاربر می‌گیره، تبدیل به int می‌کنه، و برمی‌گردونه.
def get_age():
    user_age = input("Entrt your age: ")
    return int(user_age)

print(get_age())

#تابعی به اسم total بنویس که با *args هر تعداد عدد می‌گیره و مجموعشون رو return می‌کنه.
def total(*args):
    return sum(args)

print(total(2, 5, 6))

#تابعی به اسم print_profile بنویس که با **kwargs اطلاعات یه شخص رو می‌گیره (مثل name, age, city) و همه‌شون رو خط به خط چاپ می‌کنه.

def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":",  value)
    
    
print_profile(name = "ali", age = 25, city = "london")




