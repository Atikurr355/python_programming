# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# prime = {2, 3, 5, 8}
#
# # a =""
# # print(a)
# # n = 10
# # while n:
# #     for i in range(n):
# #         a.append(i)
# #         n += 1
# #
# # print(a)
#
# # U = odds.union(evens)
# # print(U)
# # i = odds.intersection(evens)
# # print(i)
# #
# # u = odds.union(prime)
# # print(u)
# # iu = odds.intersection(prime)
# # print(iu)
#
# diff = odds.difference(evens)
# print(diff)
# # diff2 = evens.difference(odds)
# # print(diff2)
# l = [1, 2, 3, 4, 4, 6, 2, 3, 'abc', 'abc', 5, 6, 7, ]
# no_duplicate_set = set(l)
# print(no_duplicate_set)
# no_duplicate_list = list(no_duplicate_set)
# print(no_duplicate_list)
#
# s = {'blackbary', 'bluebary', }
#
# s.add('banana')
# s.add('apple')
#
# print(s)

library1 = {'Harry potter', 'Hunger Games', 'Lord of the Rings'}
library2 = {'Harry potter', 'Romeo Juliet'}
# all_books_in_the_town =library1.union(library2)
# all_books_in_the_town2 =library1.intersection(library2)

print(f"{library1.union(library2)}\n --------------------------------------")
print(f"{library1.intersection(library2)}\n --------------------------------------")
print(f"{library1.difference(library2)}\n --------------------------------------")
print(f"{library2.difference(library1)}\n --------------------------------------")
