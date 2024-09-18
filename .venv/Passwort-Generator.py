import random

#possible chars
chars = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "1234567890",
    "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]

passwort = ""

#Randomly generate a password with 16 characters

for i in range(16):
    char_set = random.choice(chars)
    passwort+= random.choice(char_set)

print(passwort)
#Check if password is secure

lowercase_counter = 0
uppercase_counter = 0
digit_counter = 0
symbol_counter = 0

#count numbers of chars
for i in passwort:
    if i in chars[0]:
        lowercase_counter+= 1
    elif i in chars[1]:
        uppercase_counter+=1
    elif i in chars[2]:
        digit_counter+=1
    elif i in chars[3]:
        symbol_counter+=1

#check if every char is used

if lowercase_counter >= 1 and uppercase_counter >= 1 and digit_counter >= 1 and symbol_counter >= 1:
    print(f"{passwort} is secure and accepted!")
else:
    print("Please generate secure password with minimum of 1 lower,upper,digit and symbol character")
