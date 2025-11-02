#Q1 : print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#Q2: print even numbers from 1 to 20.
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#Q3: print numbers from 10 to 1 (reverse)
for i in range(10,0,-1):
    print(i)

#Q4 :sum of first 10 natural numbers.
total = 0
for i in range(1,11):
    total += i
    print("Sum is:",total)


#Q5:print "Hello" 5 times using while loop.
count = 1
while count <= 5:
    print("hello")
    count += 1


#Q6: countdown from 5 to 1.
n = 5
while n > 0:
 print(n)
 n -= 1


#Q7: multiplication table(user input)
num = int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num * i)


#Q8: print star patterns.
for i in range(1,6):
    print("*" * i)


#Q9: keep asking users name untill they type "stop".
while True:
    name = input("Enter your name(type 'stop' to exit):")
    if name.lower()== "stop":
        break
        print("Hello",name)