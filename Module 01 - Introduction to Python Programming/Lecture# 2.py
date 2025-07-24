str1 = "Hafiz Salman"
len1 = len(str1)
print(len1)

str2 = "Gaming Experince"
len2 = len(str2)
print(len2)
final_str = str1 +" "+ str2 
print(final_str)
print(len(final_str))






 #indexing




str = "Hafiz Salman"
ch = str[1]
print(ch)






# #slicing



str = " Welcome to Lahore"
print(str[12:18])



#string Function


str = "i am learning python from AppnaCollege"
print ( str.replace ("python","Java" ))






#WAP to input user's first name & print in lenght



name = input("Enter Your Name : ")
print( " lenght of ypur name " , len(name))




#WAP to find the occurrence of $ in a string


str = "The price of this product is $20"
print (str.count("$"))




#Conditional Statement


age = int(input("enter your age "))

if age >= 18 and age < 30 :
    print(age)
else:
    print("Not Available")





# Grade student based on marks


marks = int(input("Enter Your Marks: "))

if marks >= 90:
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"   
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print( "grade of the student -->", grade)       


  




#WAP to Find the largest number entered by the user is odd or even

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

if ( a >= b and a >= c and a>= d):
    print("First Number is Largest:" , a)
elif( b >= c and b >= d):
    print("Second Number is Largest:" , b)
elif(c >= d):
    print("Third Number is Largest: " , c)    
else:
    print("Fourth Number is Largest: ", d)    





#WAP to check if a number is a multiple of 7 or not

num = int(input("Enter Number: "))


if(num % 7 == 0 ):
    print(num,"is Multiple of 7 ")

else:
    print("Not Multiple of 7 ")