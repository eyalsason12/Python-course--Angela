
print("Please enter the coordinates of the 3 " +
"vertices of the first triangle:")
print("Enter the first vertex (2 real numbers)")
x1 = float(input("first x:"))
y1 = float(input("first y:"))
print("Enter the second vertex (2 real numbers)")
x2 = float(input("second x:"))
y2 = float(input("second y:"))
print("Enter the third vertex (2 real numbers)")
x3 = float(input("third x:"))
y3 = float(input("third y:"))

a1 = (((x2-x1)**2)+((y2-y1)**2))**0.5
b1 = (((x3-x2)**2)+((y3-y2)**2))**0.5
c1 = (((x1-x3)**2)+((y1-y3)**2))**0.5

print("Please enter the coordinates of the 3 " +
"vertices of the second triangle:")
print("Enter the first vertex (2 real numbers)")
x11 = float(input("first x:"))
y11 = float(input("first y:"))
print("Enter the second vertex (2 real numbers)")
x12 = float(input("second x:"))
y12 = float(input("second y:"))
print("Enter the third vertex (2 real numbers)")
x13 = float(input("third x:"))
y13 = float(input("third y:"))

a2 = (((x12-x11)**2)+((y12-y11)**2))**0.5
b2 = (((x13-x12)**2)+((y13-y12)**2))**0.5
c2 = (((x11-x13)**2)+((y11-y13)**2))**0.5

print("The first triangle is (" + str(x1) + ",", str(y1) + ")" + " " + "(" + str(x2) + ",",str(y2) + ")" + " " + "(" + str(x3) + ",", str(y3) + ")")
print("Its lengths are "+str(a1) + "," + str(b1) + "," + str(c1))
print("The second triangle is (" + str(x11) + ",", str(y11) + ")" + " " + "(" + str(x12) + ",", str(y12) + ")" + " " + "(" + str(x13) + ",", str(y13) + ")")
print("Its lengths are "+str(a2) + "," + str(b2) + "," + str(c2))
if a1 == b2:
    if (b1 == c2 and c1 == a2) or (b1 == a2 and c1 == c2):
        print("The triangles are congruent.")

elif a1 == a2:
    if (b1 == b2 and c1 == c2) or (c1 == b2 and b1 == c2):
        print("The triangles are congruent.")
elif a1 == c2:
    if (b1 == a2 and c1 == b2) or (b1 == b2 and c1 == a2):
        print("The triangles are congruent.")
else:
    print("The triangles are not congruent.")