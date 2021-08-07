import sys
import timeit

my_list = ["Atik",29,"dhaka"]
my_tuple = ("Atik",29,"dhaka",)

print("list",sys.getsizeof(my_list),"bytes")
print("tuple",sys.getsizeof(my_tuple),"bytes")


print(timeit.timeit(stmt="[1,2,3,4,5]", number=100000))
print(timeit.timeit(stmt="(1,2,3,4,5)", number=100000))

