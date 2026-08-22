try:
    ages = {"جمارو": 25}
    print(ages["رضا"])
except KeyError:
    print("این اسم توی دیکشنری نیست")
except ValueError:
    print("مقدار نامعتبره")
finally:
    print("پایان بررسی")