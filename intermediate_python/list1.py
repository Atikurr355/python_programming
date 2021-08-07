import os

names = ['tanbir', 'ishan', 'rayhan', 'arian', 'miraz', 'snigda', 'chowa', 'joynob', 'nusrat', 'monika']

# for name in names:
#     print(f"Hello,{name}")


# for name in names:
#     print(''.join(["Hello," + name]))

# print(', '.join(names))
#
# open_file_location='D:\python_programming'
# file_name = '01.py'
# print(open_file_location +'\\' + file_name)
#
# with open(os.path.join(open_file_location,file_name)) as f:
#     print(f.read())

who = 'Arian'
how_many = 22

# if "arian" in names:
#     print("Arian brought " + str(how_many) + " apples today")
#
# else:
#     print(f"You entered the name out of list! ")

print(who, "brought ",how_many," apples")
print('{} brought {} apples today'.format(who, how_many))

#reverse string
name="Atik"
print(name[::-1])
