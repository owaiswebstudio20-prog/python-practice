#LAB 2
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

#LAB 3
#1)
print("Hello World!") # without /b code

#2)
# Taking two numbers from the user
first_number = str(input("28"))
second_number = str(input("06"))

# Adding both numbers
sum = (first_number + second_number)

# Displaying the result
print("Addition of two number is: ", sum)

#3
#age = 23
#message = "Happy " + age + "rd Birthday!"
#print(message)
#Python mein String (text) aur Integer (number) ko directly + se join nahi kar sakte

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
#correct code. Yahan str(age) number 23 ko text mein convert kar raha hai.

#4
#STUDENT BIO DATA
print("STUDENT BIO DATA")

dob = input("Enter Date of Birth:")
roll_no = input("Enter Roll Number:")
section = input("Enter section:")
Matric_percentage = input("Enter Matric Percentage:")
Matric_grade = input("Enter Matric Grade:")
Inter_percentage = input("Enter Intermediate Percentage:")
Inter_grade = input("Enter Intermediate Grade:")

print("\n----- STUDENT DETAILS -----")
print("Date of Birth :",dob)
print("Roll Number :",roll_no)
print("Section :",section)
print("Matric Percentage :",Matric_percentage)
print("Matric Grade :",Matric_grade)
print("Intermediate Percentage :",Inter_percentage)
print("Intermediate Grade :",Inter_grade)



#5
food = input("What food would you like? ")

print("Let me see if I can find you a", food.upper())

#6
course1 = int(input("Enter course 1 marks: "))
course2 = int(input("Enter course 2 marks: "))
course3 = int(input("Enter course 3 marks: "))
course4 = int(input("Enter course 4 marks: "))
course5 = int(input("Enter course 5 marks: "))

total_marks = course1 + course2 + course3 + course4 + course5

average = total_marks / 5

percentage = (total_marks * 100) / 250

print("Total Marks:", total_marks)
print("Average:", average)
print("Percentage:", percentage)
