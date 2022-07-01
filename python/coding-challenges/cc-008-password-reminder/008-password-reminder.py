#Assignment - 011/01 (Password Reminder)

#To improve your conditional algorithm and string operations skills.


#Task : Let's say; you left a message in the past that prints a password you need. 
# To see the password you wrote, you need to enter your name and the program should recognize you.
#Write a program that 

#Takes the first name from the user and compares it to yours,
#Then if the name the user entered is the same as yours, 
# print out such as : "Hello, Joseph! The password is : W@12",

#If the name the user entered is not the same as yours, 
# print out such as : "Hello, Amina! See you later."

name = input("please, enter your name: ")

admin = 'Volkan'
password = 'Aa1234'
if name.capitalize() == admin:
    print("Hello, {}! The password is : {}".format(admin, password))
else:
    print("Hello, {}! See you later.".format(name))


