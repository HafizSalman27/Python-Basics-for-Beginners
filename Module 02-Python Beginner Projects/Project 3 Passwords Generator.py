# Special Program: Passwords Generator


import string
import random

pwd_len = int(input('Enter Password lenght: '))
pwd = []

low_str = string.ascii_lowercase
upp_str = string.ascii_uppercase
dit_str = string.digits
pun_str = string.punctuation

pwd.extend(list(low_str))
pwd.extend(list(upp_str))
pwd.extend(list(dit_str))
pwd.extend(list(pun_str))

random.shuffle(pwd)
print ("".join(pwd[0:pwd_len]))
