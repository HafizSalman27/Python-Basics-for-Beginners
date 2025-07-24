# Function in Python


def calc_sum (a, b):    # Parameters
    sum = a + b
    print (sum)
    return sum


calc_sum(5, 10)       # Function Call

calc_sum(4, 15)

calc_sum(8, 67)


# Let's Practice 


# WAF to print the length of a list. ( list is the parameter)

cities = ["lahore", "Karachi", "Islamabad", "Hyderabad", "Multan"]
heroes = ["ironman", "superman", "thor", "hulk"]

def print_len (list):
    print(len(list))

print_len(cities)
print_len(heroes)


# WAF to print the elements of a list in a single line. (list is the parameter)


cities = ["lahore", "Karachi", "Islamabad", "Hyderabad", "Multan"]


def print_list (list):
    for item in list:
        print(item, end= "\n")


print_list(cities)



# WAF to find the factorial of n. (n is the parameter)


n = 5
fact = 1
for i in range (1, n+1):
    fact *= i

print(fact)



#  WAF to convert USD to PKR




def covert (usd_avl):
    pkr_val = usd_avl * 280
    print(usd_avl, "USD", pkr_val, "PKR")

covert(2)



#Write a function that takes a number from the user and prints "Positive" if it’s greater than 0, otherwise prints "Non-positive".


num = int(input("Enter a number: "))

def check_positive_or_nonpositive():
    if (num > 0):
        print ("Number is positive")
    else:
        print ("Number is Non Positive")
    
check_positive_or_nonpositive()


# Recursion in Python


def show(n):

    if (n == 0):
        return
    print(n)
    show(n-1)

show(10)     



# Let's Practice

# Write a recursive function to calculate the sum of first n natural numbers.

def natural (n):

    if ( n == 0):
        return 0
    return natural( n - 1) + n

print (natural(5))



# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameter

fruits = ["mango", "litchi", "apple", "banana"]

def print_list (list, idx = 0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

print_list (fruits)