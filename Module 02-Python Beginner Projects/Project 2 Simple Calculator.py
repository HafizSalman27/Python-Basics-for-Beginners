# Special Program: Simple Calculator

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

operator = input('Enter operator: ')

if operator == "+":
    print ('The Sum of two number is: ', num1+num2)
elif operator == "-":
    print ('The Sub of two number is: ', num1-num2)
elif operator == "*":
    print ('The Multiplication of two number is: ', num1*num2)
elif operator == "/":
    print ('The division of two number is: ', num1/num2)       
else:
    print ('Enter the integer values')        