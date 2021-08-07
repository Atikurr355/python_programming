def profile(**person):
    print(person)

    def display(k):
        if k in person.keys():
            print(f'{k} = {person[k]}')

    display('name')
    display('age')
    display('pet')


profile(name="atik", age=28, pet="max")
