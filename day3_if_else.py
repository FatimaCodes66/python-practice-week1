#Q1: check if a number is positive r negative

num = int(input("enter a number:"))
if num > 0:
    print("Positive number:")
else:
    print("negative number:")

#Q2 : check if a person is eligible to vote(age 18 +)
age = int(input("enter your age:"))
if age >= 18:
    print("eligible to vote:")
else:
    print("not eligible to vote:")

#Q3 :check if number is even or odd.

num = int(input("enter a number:"))
if num % 2 == 0:
    print("num is even:")
else:
    print("num is odd:")

#Q4 :Password check.
password = int(input("enter password:"))
if password == "python123":
    print("access granted:")
else:
    print("Access denied:")

#Q5 :grade check.
marks = int(input("enter marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("fail")


#Q6 : print the larger of two numbers.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a > b:
    print("the larger number is a",a)
elif b > a:
    print("the larger number is b",b)
else:
    print("both numbers are equal")


#Q7 : shopping discount system

amount = float(input("enter total bill amount:"))
if amount > 2000:
    discount = amount * 0.20
    final_amount = amount - discount
    print("you got 20% discount. final amount to pay:",final_amount)
elif amount > 1000:
    discount = amount * 0.10
    final_amount = amount - discount
    print("you got 10% discount.final amount to pay:",final_amount)
else:
    print("No discount.final amount to pay:",amount)


#Q 8: logic system wit two conditions.
username = input("enter username:")
password = input("enter pasword:")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


#Q 9 : check if number is divisible by both 3 nd 5.
num = int(input("enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print("divisible by both 3 and 5")
else:
    print("Not divisible by bot 3 and 5")