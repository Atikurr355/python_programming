def grad():
    subject = ['Bangla', 'English', 'Maths', 'General Science', 'Social Science', 'Religion', 'ICT']
    for i in range(sub):
        marks = int(input(f"Enter marks of {subject[i]} subject: "))
        if marks <= 0 and marks > 100:
            print("you entered invalid marks!")
        elif marks >= 80 and marks <= 100:
            print("You got A+")
        elif marks >= 70 and marks <= 80:
            print("You got A")
        elif marks >= 60 and marks <= 70:
            print("You got A-")
        elif marks >= 50 and marks <= 60:
            print("You got B")
        elif marks >= 45 and marks <= 50:
            print("You got C")
        elif marks >= 40 and marks <= 45:
            print("You got D")
        elif marks >= 0 and marks <= 40:
            print("You got F")
        else:
            print("Invalid operations")

print(f"Enter the marks according to this order: subject=['Bangla', 'English', 'Maths', 'General Science', 'Social Science', 'Religion', 'ICT']")
sub = int(input("Enter how many subject:"))
result =grad()

print(sum(result))

python.done()

