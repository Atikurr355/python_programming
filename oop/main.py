from class1 import Person


class Student(Person):
    pass


name=input("Enter your name: ")
age = input("Enter your age: ")

p1 = Student(name, age)
print(f"Name: {p1.name}, age: {p1.age}")