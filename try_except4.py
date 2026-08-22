class NegativeAgeError(Exception):
    pass

class AgeTooHighError(Exception):
    pass


def set_age(age):
    if age < 0:
        raise NegativeAgeError("age cant be nagative.")
    if age > 150:
        raise AgeTooHighError("Age not passible.")
    else:
        return age
    
    
try:
    set_age(200)
except NegativeAgeError as e:
    print("age cant be nagative: ", e)
except AgeTooHighError as e:
    print("Age not passible: ", e)
    
    