import string
import random

# get upper case letters and lowercase letters
letters = list(string.ascii_letters)
# get digits
digits = list(string.digits)
# get special characters
special_characters = list(string.punctuation)
# connect all characters
all_characters = letters + digits + special_characters

# choice random number of length from 8 to 15
length = random.choice(range(8,15))
print(length)
password = []
# for loop for appending random characters to password
for i in range(length):
   
    # Picking a random character from character list
    randomchar = random.choice(all_characters)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))