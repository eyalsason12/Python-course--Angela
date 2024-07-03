
print("hello user,please insert 3 sides of triangle")
a = int(input("first side: "))
b = int(input("second side: "))
c = int(input("third side: "))

print("The lengths of the triangle sides are: "+str(a)+","+ str(b) + "," + str(c))

if a <= 0 or b <= 0 or c <= 0:
    print("The given three sides don't represent a triangle")
else:
    p = (a + b + c) / 2
    perimeter = a + b + c
    s_b = (p * (p - a) * (p - b) * (p - c))
    if s_b > 0:
        s = s_b ** 0.5
        print("The perimeter of the triangle is: " + str(perimeter))
        print("The area of the triangle is: " + str(s))
    else:
        print('The given three sides don'+ "'" + 't represent a triangle')
