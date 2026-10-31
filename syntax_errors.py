
#Extra colon (:) after x = 5 causes a SyntaxError remove the colon to fix it

# x = 5:
# print(x)



#Corrected code executes successfully and displays the value of x

x = 5
print(x)


#Invalid variable name and incompatible data types cause errors
# 1TEXT = "SSUET"
#  NUMBER = 1
#  print(NUMBER+ TEXT)

#Corrected the variable name and used a comma to print both values
TEXT = "SSUET"
NUMBER = 1
print(NUMBER, TEXT)

#Invalid assignment because a value cannot be assigned to a number
# a = b = 3 = 4

#Dono variables ko different values assign ki gayi hain (a = 3, b = 4)
a = 3
b = 4

print(a)
print(b)

#Expression is evaluated according to BODMAS rule.
a = 2 % 2 + 2 * 2 - 2 / 2;
print(a)

#Expression is evaluated according to BODMAS rule.
b = 3 / 2 + 5 * 4 / 3 ;
print(b)


#Expression is evaluated according to BODMAS rule.
c = b = a = 3 + 4 ;
print(c)

# Calculate the area of a circle using A = pi * r^2

pi = 3.14
r = 50
a= pi * r**2

print("Area of a circle",a)

#distance formula
x1 = 4
y1 = 3

x2 = 8
y2 = 12

# Calculate distance between two points
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance=",distance)
