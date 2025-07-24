# OOPS in Python

# class Student :
#     name = "Salman"

# s1 = Student ()
# print (s1.name)



#_ _init_ _ Function


# Default Constructors


# class Student:

#     def __init__(self):
#         pass



# Parameterized Constructors


# class Student:

#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
#         print ("Adding new students..")
        

# s1 = Student ("Hafiz", 89)
# print (s1.name, s1.marks)

# s2 = Student ("Salman", 95)
# print (s2.name , s2.marks)

# s3 = Student ("Aamir", 99)
# print (s3.name, s3.marks)




# Class & Instance Attribute


# class Student:

#     college_name = "ABCD"           # Class & Instance Attribute

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student ("Hafiz", 88)
# print (s1.name , s1.marks)

# s2 = Student ("Salman", 99)
# print (s2.name , s2.marks)       

# print (Student.college_name)



# Method


# class Student:
#     college_name = "ABCD"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome (self):                             # Method 
#         print ("Welcome Students", self.name)

#     def get_marks(self):                            # Method
#         return  self.marks

# s1 = Student ("Hafiz", 88)
# s1.welcome()

# print (s1.get_marks())




# Let's Practice


# Create student class that take name & marks of 3 subjects as arguments in constructor.
# Then create a method to print average.



# class Student :

#     def __init__(self, name, marks,):
#         self.name = name
#         self.marks = marks

#     def get_avg (self):
#         sum = 0

#         for val in self.marks:
#             sum += val
#         print ("Hi", self.name, "Your avg score is:", sum/3)


# s1 = Student ("Hafiz", [95, 82, 99])
# s1.get_avg()


# Abstraction 


# class Car ():

#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start (self):
#         self.clutch = True
#         self.acc = True
#         print("Car is started..")

# car1 = Car()
# car1.start()


# Create Account class with 2 attributes-balance & account no.
# Create methods for debit, credit & print the balance.


 

# class Account ():

#     def __init__(self, bal, acc):
        
#         self.balance = bal
#         self.account_no = acc


#     # Debit/Credit Method 

#     def debit (self, amount):
#         self.balance -= amount
#         print ("Rs.", amount, "Was Debited")
#         print ("Total balance = ", self.get_balance())


#     def credit (self, amount):
#         self.balance += amount
#         print ("Rs.", amount, "Was Credited")
#         print ("Total balance = ", self.get_balance())

#     def get_balance (self):
#         return self.balance            

# acc1 = Account (6000, 5055)
# acc1.debit (500)
# acc1.credit (600)   






# class Account ():

#     def __init__ (self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit (self, amount):
#         self.balance -= amount
#         print ("Rs.", amount, "Was debited From your account" )
#         print ("Total balance =", self.get_balance())

    
#     def credit (self, amount):
#         self.balance += amount
#         print ("Rs.", amount, "Was credited in your account")
#         print ("Total balance =", self.get_balance())

#     def get_balance (self):
#         return self.balance

# acc1 = Account (6000, 5055)
# acc1.debit (100)
# acc1.credit (200)


# Inheritance


# class Car :
#     @staticmethod

#     def start ():
#         print ("Car started..")

#     @staticmethod

#     def stop ():
#         print ("Car stopped..")


# class ToyotaCar (Car):

#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar ("Mercedes")

# print (car1.start())





# Class Method


# class Person:
#     name = "anonymous"

#     @classmethod

#     def ChangeName (cls, name):
#         cls.name = name


# p1 = Person ()
# p1.ChangeName ("Hafiz Salman Sarwar")

# print (p1.name)



# Property


# class StudentResult:

#     def __init__(self, Phy, Math, Comp):

#         self.Phy = Phy
#         self.Math = Math
#         self.Comp = Comp
        


#     @property                                                                      #Property

#     def percentage (self):

#         return str ((self.Phy + self.Math + self.Comp) / 3) + "%"   

# stu1 = StudentResult (88, 86, 87)
# print (stu1.percentage)

# stu1.Math = 80

# print (stu1.percentage)
                 

# Polymorphism





# print (1 + 2)
# print ("Hafiz" + "Salman")
# print ([1, 2, 3] + [4, 5, 6])




# class Complex:

#     def __init__ (self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber (self):
#         print (self.real , "i +", self.img, "j")



#     def __add__ (self, num2):

#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex (newReal, newImg)


           
# num1 = Complex (1, 3)
# num1.showNumber ()

# num2 = Complex (4, 6)
# num2.showNumber()


# num3 = num1 + num2
# num3.showNumber ()




# Question

#  Define a Circle class to create with radius r using the constructor.
#  Define an Area() method of the class which calculate the area of the circle.
#  Define a Perimeter() method of the class which allow you to calculate the perimeter of the circle.



# class Circle:

#     def __init__ (self, radius):

#         self.radius = radius

#     def area (self):

#         return (22/7) * self.radius

#     def perimeter (self):
#         return 2 * (22/7) * self.radius

# c1 = Circle (21)
# print (c1.area())
# print (c1.perimeter())        



# Question 


# Define a Employee class with attribute role, department & salary. This class also has a showDetails()method.
# Create an Engineer class that inherits properties from Employee & has additional attribute : name & age.






# class Employee:

#     def __init__ (self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails (self):
#         print ("role =", self.role)
#         print ("department =", self.department)
#         print ("salary =", self.salary) 



# class  Engineer (Employee):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__ ("Engineer", "IT", "70,000")



# eng1 = Engineer ("Hafiz Salman Sarwar", 30)
# eng1.showDetails()




# Question 



# Create a class called order which stores item & it's price.
# Use Dunder function __gt__() to convey that:
#                                  order > order2 if price of order2




class Order :

    def __init__ (self, item, price):
        self.item = item
        self.price = price


    def __gt__(self, odr2):
        return self.price > odr2.price    

odr1 = Order ("Chips", 30)
odr2 = Order ("Tea", 20)       

print (odr1 > odr2)








