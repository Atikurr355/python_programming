print('Create your account')
quite = input("If you want to Exit type exit otherwise press enter: ")
username = input('Enter username: ')
password = input('Enter Password: ')

print('Your account has been created successfully!')

print('---------------------------Now you can Login into your account---------------------------')

while True:
    if quite == "exit":
        break
    user = input("Inter username:")
    passd = input("Input Password: ")
    if user == username and passd == password:
        print('Welcome to your dashboard!', username)
        break
    else:
        print('Invalid Credentials!')
        quite = input("If you want to Exit type exit otherwise press enter: ")
