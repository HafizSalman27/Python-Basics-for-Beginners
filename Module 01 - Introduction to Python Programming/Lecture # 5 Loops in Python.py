

# Loop in Python

count = 2
while count <= 5:
    print("Salman")
    count += 1


# Let's Practice


# Print numbers from 1 to 100

num = 1
while num <= 100:
    print(num)
    num += 1


# Print number from 100 to 1

num = 100
while num >= 1:
    print(num)
    num -= 1


# Print the multiplication table of a number n.



num = int(input("Enter Number: "))
i = 1
while i <= 10:
    print(num*i)
    i +=1


# Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0

while i < len(num):
    print(num[i])
    i += 1


# Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 81
i = 0
while i < len(num):
    if (num[i]== x):
        print("Found", i)
    i += 1



# For loop

str = "python"

for char in str :
    print(char)
else:                   
    print("End")


# Let's Practice using for loop


# Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in num :
    print(el)


# Search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

idx = 0

for val in num:
    if (val == x):
        print("Number found", idx)
    idx += 1


# Range in Python


for el in range (5):
    print (el)
    

# Print number from 1 to 100

for val in range (1, 101):
    print (val)


# Print number from 100 to 1


for val in range (100, 0, -1):
    print(val)


# Print the multiplication of a number n.


num = int(input("Enter Number : "))

for chr in range(1, 11):
    print(num * chr)