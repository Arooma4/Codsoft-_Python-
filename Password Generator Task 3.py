print("######################## WELCOME TO RANDOM PASSWORD GENERATOR #############################")
import random
import string

length=int(input("Enter the length of password: "))
char =string.ascii_letters
char +=string.digits
char +=string.punctuation
char +=string.hexdigits
char +=string.ascii_lowercase
char +=string.ascii_uppercase
Password=''.join([random.choice(char) for i in range(length)])
print("Your random password is:",Password)
    
