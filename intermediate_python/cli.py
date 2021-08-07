def cli(x,y,operation):
    if operation == "plus":
        return x+y
    elif operation == "sub":
        return x-y
    elif operation == "mul":
        return x*y
    elif operation == "div":
        return x/y

result = cli(78,6,"plus")
print(result)