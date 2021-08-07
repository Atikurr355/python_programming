from person import Person

class Student(Person):
    def __init__(self, name: str, age: float, height: float, email_id: str, student_id: str):
        super().__init__(name, age, height)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f" Name:{self.get_name()}\n Age: {self.get_age()}\n Height: {self.get_height()}\n E-mail: {self.email}\n ID: {self.id}\n"

    def __str__(self):
        return f" Name:{self.get_name()}\n Age: {self.get_age()}\n Height: {self.get_height()}\n E-mail: {self.email}\n ID: {self.id}\n"


student = Student("Rana", 23.0, 5.5, "rana@gmail.com", "3151510067")

print(student)

student.set_name("Atik")
print(student.get_summary())