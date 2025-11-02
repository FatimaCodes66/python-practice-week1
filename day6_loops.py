#Q1: print numbers 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Q2: sum of numbers from 1 to 50.
total = 0
for i in range(1,51):
    total += i
    print("The sum is:",total)


#Q3 : multiplication table.
num = int(input("Enter number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)


#Q4: coutn down using while loop.
num = 10
while num >= 1:
    print(num)
    num -= 1



#Q5 :print even numbers(1 to 20)
for num in range(1,21):
    if num % 2 == 0:
        print(num)


#Q6: reverse a string.
word = input("Enter a word:")
reversed_word = word[::-1]
print("Reversed:",reversed_word)