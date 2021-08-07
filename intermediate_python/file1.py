coun_file = open('main.py', 'r')
# print(coun_file.readlines())
for lines in coun_file.readlines():
    print(lines)
coun_file.close()
