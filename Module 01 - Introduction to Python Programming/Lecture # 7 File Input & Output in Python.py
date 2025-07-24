# File I/O n Python

# f = open ( "demo.txt", "r")
# print(f.read())
# f.close()



# Let,s Practice

# Create a new file "practice.tex" using Python. Add the following data in it:

#   Hi everyone
#   We are Learning file I/O 
#   using Java.
#   I Like programming in Java.



# f = open ("practice.txt", "w")
# f.write("Hi everyone\nwe are learning file I/O")
# f.write("\nusing Java.\nI Like programming in Java.")

# f.close()


# WAF replaces all occurrences of "Java" with "Python" in above file.



# f = open ("practice.txt", "r+")

# data = f.read()
# new_data = data.replace ("Java", "Python")

# print(new_data)

# f = open ("practice.txt", "w")
# f.write(new_data)


# Search if the world "learning" exist in the file  or not.

# word = "learning"
# with open ("practice.txt", "r")  as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")    


# WAF to find in which line of the file does the word "learning" occur first.
# Print -1 if word not found.
 
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open ("practice.txt", "r") as f:
#         while data :
#             data = f.readline()
#             if ( word in data):
#                 print (line_no)
#                 return
#             line_no += 1
#     return -1
# print (check_for_line())     



# From a file containing numbers separated by commma, print the count of even numbers.

# count = 0
# with open ("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if ( int(val) % 2 == 0):
#             count += 1
# print(count)            