class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(self.name, "says", self.sound)

dog = Animal("Dog", "Woof")
dog.make_sound()


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
        
    def accelerate(self):
        self.speed = self.speed + 10
        return self.speed
        # اینجا سرعت رو ۱۰ واحد زیاد کن
    
    
        
class Counter:
    def __init__(self):
        self.count = 0
    def increase(self):
        self.count += 1
        self.print_count()  # اینجا مشکل داره
    def print_count(self):
        print(self.count)

c = Counter()
c.increase()