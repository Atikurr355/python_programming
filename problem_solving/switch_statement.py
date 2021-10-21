area = "triangle";
PI = 3.142
l = 5
b = 4
r = 3

switch(area):
    case 'circle':
        console.log("\nthe ara of a circle is: " + PI*r**2)
        break
    case 'triangle':
        console.log("\nthe ara of a triangle is: " + (l*b)/2)
        break
    case 'rectangle':
        console.log("\nthe ara of a rectangle is: " + (l*b))
        break
    default:
        console.log("\nPlease Enter valid data!")
}