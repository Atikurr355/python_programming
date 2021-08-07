class Person:
    def __init__(self, name: str, age: float, height: float):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("sorry number and special can not be contain in name")
            return
        self.__name = new_name

    def __has_any_number(self, st):
        # l = "0><=+%$@#123456789"
        # for i in l:
        #     st = i
        # return st
        return "0" in st

    def get_summary(self):
        return f"Name: {self.__name}, Age: {self.__age}, Height: {self.__height}"


# preson_list = [
#     Person("Atik", 29.0, 5.5),
#     Person("rana", 23.0, 5.5),
#     Person("fizz", 29.0, 5.5),
#     Person("shakib", 27.0, 5.5),
#     Person("masud", 29.0, 5.5),
#     Person("kona", 23.0, 5.5)
# ]
#
# for i in preson_list:
#     if i.get_age() > 23.0:
#         print(i.get_summary())
