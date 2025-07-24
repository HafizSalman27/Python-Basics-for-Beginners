# Dictionary in Python

 dict = {
     "name" : "Hafiz Salman",
     "age" : 20,
     "subjects" : ["python", "C", "Java"],
     "male" : "yes",
     22 : 21.5
 }
 print(dict)


#Nested Dictionary

 student_info = {

     "name" : "Hafiz Salman",

     "subject" : {

         "Phy" : 75,
         "Math" : 80,
         "Eng" : 90,

     }
 }

 print(student_info)


# Set in Python

 set = {1, 2, 3}
 print(set)
 print( type(set))


# Method of Set

# Add Method

 set = set ()
 set.add(1)
 set.add(2)
 set.add(3)

 print(set)


# Remove Method



 set = set ()

 set.add (1)
 set.add (2)
 set.add (3)

 set.remove (3)

 print (set)





# Clear Set   #set.clear

 set = set ()

 set.add (1)
 set.add (2)
 set.add (3)

 set.clear()

 print(len(set))



# Practice Questions


# Storing word meaning in Python

 dict = {
     "table" : ["a piece of furniture", "list of fact & figures"],
     "cate" : " a small animal"
 }

 print(dict)


# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.


 set = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c"}

 print(len(set))

# WAP to enter marks of 3 subjects form the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

 marks = {}



 sub1 = int(input("Enter Phy: "))
 marks.update ({"Phy": sub1})

 sub2 = int(input("Enter Math: "))
 marks.update({"Math": sub2})

 sub3 = int(input("Enter Eng: "))
 marks.update({"Eng": sub3})


 print(marks)



set = {1, 2, 3}

set.store { 9, 9.0}
print(set)
