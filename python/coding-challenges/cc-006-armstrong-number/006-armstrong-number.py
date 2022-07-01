'''
Find out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 3**3 + 7**3 + 1**3;
9474 = 9**4 + 4**4 + 7**4 + 4**4;
93084 = 9**5 + 3**5 + 0**5 + 8**5 + 4**5.

Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user.

'''
no = int(input("\nEnter a pozitive integer number: ").strip())

if no > 0:
    sum_num = 0
    n_times = 0
    num = no
    while num > 0:
        n_times += 1
        num //= 10

    num = no
    while num > 0:
        modulus_num = num % 10
        print(modulus_num)
        sum_num += (modulus_num ** n_times)
        print(sum_num)
        num //= 10
        print(num)

    if no == sum_num:
        print("{} is an armstrong number".format(no))
    else:
        print("{} is not an armstrong number".format(no))
elif no == 0:
    print("{} is a Zero!!, please enter pozitive integer number: ".format(no))         
else:
    print("{} is an invalid entry. Don't use non-numeric, float, or negative values: ".format(no))        

