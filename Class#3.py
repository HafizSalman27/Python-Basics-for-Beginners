#List in Python

marks = [32.2, 24.5, 45.2, 22.3, 24.3]
print(marks)
print(len(marks))
print(marks[1])
print(marks[2])
list = [24, 35, 45, 58, 48, 145]

print(list[4:6])


#list Slicing


student_list = [25, 45, 35, 78, 63, 44, 79, 55]
print(student_list[-5:-2])


#list Methods



list = [0, 1, 2, 3, 4, 5]
print(list.append(6))
print(list.append(7))
print(list.sort())
print(list)



#Reverse = True



list = [0, 1, 2, 3, 4, 5]
print(list.sort(reverse=True))
print(list)


#Insert Method


list = [5, 2, 3, 7, 9, 6]
list.insert(2,1)
print(list)




#Remove Method


list = [3, 1, 2, 1]
list.pop(2)
print(list)


#Tuples in Python


tup = (4, 5, 7)
print(tup[1:3])


#tup.index/count



tup = (2, 4, 6, 5, 6)
print(tup.count(6))


#WAP to ask the user to enter name of their 3 favorite movies & store them in a list



movies_list = []
mov1 = input("Enter 1st Movie: ")
mov2 = input("Enter 2nd Movie: ")
mov3 = input("Enter 3rd Movie: ")

movies_list.append(mov1)
movies_list.append(mov2)
movies_list.append(mov3)
print(movies_list)


#WAP to check if a list contain a palindrome of elements


list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list2 = list2.reverse()

if (copy_list1 == list1):
    print("List1 is a palindrome")
else:
    print("Not palindrome")



#WAP to count the number of students with "A" grade in the following tuple


tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))


#Store the above values in a list & sort them form "A" to "D"


list = ["C", "D", "A", "A", "B", "B", "A"]

print(list.sort(), list)







