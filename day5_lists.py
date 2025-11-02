#Q1: create a list of 5 fruits and print all items.
fruits = ["apple","banana","mango","orange","grapes"]
print(fruits)

#Q2: print only the 1st and 3rd item.
print(fruits[0])
print(fruits[2])

#Q3: replace "banana" wit "kiwi".
fruits[1]= "Kiwi"
print(fruits)


#Q4: add new fruit to the list.
fruits.append("pineapple")
print(fruits)

#Q5 : remove any one fruits from the list.
fruits.remove("orange")
print(fruits)

#Q6 : loop through list and print each item.
for item in fruits:
    print(item)


#Q7 : store 5 numbers and  print sum of all numbers.
numbers = [10,20,30,40,50]
total = sum(numbers)
print("sum",total)

#Q8: print only numbers greater than 25.

for n in numbers:
    if n > 25:
        print(n)


#MINI PROJECT:
#shopping cart items.
cart = []
for i in range(5):
    item = input("Enter item:")
    cart.append(item)
    print("Your Shopping Cart:",cart)
