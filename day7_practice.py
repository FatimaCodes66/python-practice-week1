#Q1: check even or odd user input.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("even")
else:
    print("Odd")


#Q2: password checker.
password =input("enter password:")
if password =="python123":
    print("Access granted")
else:
    print("Access denied")


#Q3: coutn digits in a number.
number = input("Enter a number")
count = len(number)
print("Total digits:",count)


#Q4:star pattern.
for i in range(1,6):
    print("*"*i)


#Q5: largest among 3 numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if num1 > num2 and num1 >num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3
print("largest number is:",largest)



#Q6: number guessing (simple).
secret = 7
num = int(input("Enter number:"))
if num == secret:
    print("Correct")
else:
    print("Try again")