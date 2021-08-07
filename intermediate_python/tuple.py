# a = (1,2,3,4,5,6,7,8,9,10,)
# print(a)
# print(a[::-1])
# my_tuple = ("Atik",29,"Dhaka")
# name,age,city = my_tuple
# print(name)
# print(age)
# print(city)
#
# # unpacking tuple
# i1,*i2,i3,i4,i5 = a
# print(i3)

# t = (1, 2, 3)
#
# credit_card1 = (1234123412341234, 'atik vai', '11/21', 1234)
# credit_card2 = (1234123412341234, 'atik vai', '11/21', 1234)
#
# credit_cards = [credit_card1, credit_card2]
#
# print(credit_cards)
person = ("Akhi-Rahman", 25, 'pizza')
person1 = ("Akhi-Rahman", 25, 'pizza')
person2 = ("Atikur-Rahman", 28, 'mutton')

people = [person1, person2]

name, age, favfood = person

print(name)
print(age)
print(favfood)
print('--------------------------------------------------------')

for name, age, favfood in people:
    print(f' Name: {name}\n Age: {age}\n Favorite Food: {favfood}\n--------------------------------')
