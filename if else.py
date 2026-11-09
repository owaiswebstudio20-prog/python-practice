# Incorrect variable declaration
a = 500,b,c;

# Check if a is greater than or equal to 400
if ( a >= 400 ):
    b = 300
    c = 200
    # Display the values
    print("Value is:", b, c)

a = 500  # Assign value to a

if a >= 400:  # Check the condition
    b = 300
    c = 200
    print("Value is:", b, c)  # Display values

number = int(input("Enter an integer: "))  # Get integer input

print(type(number))  # Display data type

if number % 5 == 0:  # Check divisibility by 5
    print("HiFive")  # Print HiFive
else:
    print("No answer")  # Print No answer

#if score >= 60.0
 #   grade = 'D'
#elif score >= 70.0
 #   grade = 'C'
#elif score >= 80.0
 #   grade = 'B'
#elif score >= 90.0
 #   grade = 'A'
#else:
 #   grade = 'F'
#correct program
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)

requested_topping = 'anchovies'

# Check kar rahe hain ke value anchovies ke equal nahi hai
if requested_topping != 'anchovies':

    # Sirf condition TRUE hone par print hoga
    print("Hold the anchovies!")

num = 3  # Assign value

if num >= 0:  # Check if non-negative
    print("Positive or Zero")
else:
    print("Negative number")

num = 5  # Assign value

if num >= 0:  # Check if number is non-negative
    print("Positive or Zero")
else:  # Runs if number is negative
    print("Negative number")

age = 15

if age < 4:
    price = 0
elif age < 18:
    price = 1500
else:
    price = 2000

print("Your admission cost is Rs" + str(price) + ".")

num = int(input("Enter a number: "))  # Get number from user

if num % 2 == 0:  # Check if number is even
    print("Even Number")  # Display even number
else:
    print("Odd Number")  # Display odd number

years = int(input("Enter years of service: "))  # User se service ke years lena
qualification = input("Enter qualification: ")  # User se qualification lena

if years >= 10 and qualification == "Masters":  # 10 ya zyada years aur Masters check karna
    salary = 150000

elif years >= 10 and qualification == "Bachelors":  # 10 ya zyada years aur Bachelors check karna
    salary = 100000

elif years < 10 and qualification == "Masters":  # 10 se kam years aur Masters check karna
    salary = 100000

elif years < 10 and qualification == "Bachelors":  # 10 se kam years aur Bachelors check karna
    salary = 70000

else:  # Agar koi bhi condition match na ho
    salary = 0

print("Your Salary is:", salary)  # Final salary display karna

age = int(input("Enter your age: "))  # User se age lena

if age < 2:  # Check if age is below 2
    print("Baby")

elif age < 4:  # Check if age is below 4
    print("Toddler")

elif age < 13:  # Check if age is below 13
    print("Kid")

elif age < 20:  # Check if age is below 20
    print("Teenager")

elif age < 65:  # Check if age is below 65
    print("Adult")

else:  # If all conditions are false
    print("Elder")
