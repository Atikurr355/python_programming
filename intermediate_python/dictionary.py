# my_dic = {"name":"Atik","age":29,"city":"dhaka"}
# print(my_dic)
# # my_dic2 = dict(name="Thamina",age=22,city="dhaka")
# my_dic3 = {"name":"Atik","age":29,"city":"dhaka","email":"atikurrahmanm3@gmail.com"}
# print(my_dic3)
# print("===============================================")
# #
# # print(my_dic["name"])
# # print(my_dic2['name'])
# # my_dic["email"]="atikurrahmanm3@gmail.com"
# # print(my_dic)
# # del my_dic["email"]
# # print(my_dic)
# #
# # if "name" in my_dic:
# #     print(my_dic["name"])
# #
# #
# #
# #
# # try:
# #     print(my_dic["lastname"])
# # except:
# #     print("Error")
#
# # loope
# # for key in my_dic:
# #     print(key)
# #
# # for val in my_dic.values():
# #     print(val)
# # print("Keys            values")
# # print("-------------------------------")
# # for key,val in my_dic.items():
# #     print(f"{key}              {val}")
#
# # copy dictionary
#
# # my_dic_copy = my_dic.copy()
# # my_dic_copy["email"]="atikurrahmanm3@gmail.com"
# # print(my_dic_copy)
# # print(my_dic)
#
# # dictonary update
#
# my_dic.update(my_dic3)
# print(my_dic)
# print(my_dic3)

my_dic = {"name": "Atik", "age": 25, "city": "dhaka", "email": "atikurrahmanm3@gmail.com"}
my_dic["degree"] = "BSc in CSE"

print(my_dic)

my_dic.pop("name")
print(my_dic)
for i in my_dic.items():
    print(i)
