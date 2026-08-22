class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Unknown sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


a1 = Animal("Unknown animal")
a1.speak()
d1 = Dog("Rex")
d1.speak()
c1 = Cat("Whiskers")
c1.speak()
