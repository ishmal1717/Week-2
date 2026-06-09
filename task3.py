import random
length = int(input("Enter password length:"))
use_upper = input("include upper case letters?(yes/no):").lower()
use_lower = input("include lower case letters?(yes/no):").lower()
use_digits = input("include digit?(yes/no):").lower()
use_special = input("include special characters?(yes/no):").lower()

characters = ""

if use_upper == "yes":
 characters = characters + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if use_lower == "yes":
 characters = characters + "abcdefghijklmnopqrstuvwxyz"
if use_digits == "yes": 
 characters = characters + "0123456789"
if use_special == "yes":
 characters = characters + "!@#$%^&*()"
if characters == "":
 print("Error!You must select at least one type.")
else:
 password = " "
 for i in range(length):
     password = password + random.choice(characters)
print("Generated password:",password)
