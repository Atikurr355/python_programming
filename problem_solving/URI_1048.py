# salary = float(input())
#
# if salary >= 0 or salary <= 400.00:
#     reajuste_ganho = salary / 100 * 15
#     new_salary = salary + reajuste_ganho
#     percentage = 15
#
# elif salary >= 400.01 or salary <= 800.00:
#     reajuste_ganho = salary / 100 * 12
#     new_salary = salary + reajuste_ganho
#     percentage = 12
#
# elif salary >= 800.01 or salary <= 1200.00:
#     reajuste_ganho = salary / 100 * 10
#     new_salary = salary + reajuste_ganho
#     percentage = 10
#
# elif salary >= 1200.01 or salary <= 2000.00:
#     reajuste_ganho = salary / 100 * 7
#     new_salary = salary + reajuste_ganho
#     percentage = 7
#
# elif salary >=2000.00:
#     reajuste_ganho = salary / 100 * 4
#     new_salary = salary + reajuste_ganho
#     percentage = 4
#
# print("Novo salario : %.2f" % new_salary)
# print("Novo salario : %.2f" % reajuste_ganho)
# print("Em percentual: {} {}". format(percentage,"%"))


s = float(input())
if (s >= 0 and s <= 400):
    r = s * 0.15
    n = s + r
    p = 15
elif (s >= 400.01 and s <= 800.00):
    r = s * 0.12
    n = s + r
    p = 12
elif (s >= 800.01 and s <= 1200.00):
    r = s * 0.1
    n = s + r
    p = 10
elif (s >= 1200.01 and s <= 2000.00):
    r = s * 0.07
    n = s + r
    p = 7
elif (s > 2000):
    r = s * 0.04
    n = s + r
    p = 4
print("Novo salario: %.2f" % n)
print("Reajuste ganho: %.2f" % r)
print("Em percentual: {} {}".format(p, "%"))

