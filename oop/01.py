from person import Person

# This is single line comments
print("hello world")

# # l = ['0', '>', '>', '=', '+', '%', '$', '@', '#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l = "0><=+%$@#123456789"
# for i in l:
#     print(i)
# print(i)
preson_list = [
    Person("Atik", 29.0, 5.5),
    Person("rana", 23.0, 5.5),
    Person("fizz", 29.0, 5.5),
    Person("shakib", 27.0, 5.5),
    Person("masud", 29.0, 5.5),
    Person("kona", 23.0, 5.5)
]

for i in preson_list:
    if i.get_age() > 23.0:
        print(i.get_summary())