class Person:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def eat(self):
        print("eating")

    def walk(self):
        print("Walking")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student(Person):
    roll = 315151021
    marks = "60%"

    def takeClass(self):
        print("Taking class")


Rahim = Student("Rahim", 28, "male", 6.10)
print(Rahim.eat())
print(Rahim.roll)
print(Rahim.getName())
print(Rahim.takeClass())
