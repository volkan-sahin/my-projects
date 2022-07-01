# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

# The desired output is like this:

# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fibonacci_list = []
i = 0
next_i = 0
last_i = 1
for i in range(0,11):
    
    i = next_i
    next_i = last_i
    last_i = i + next_i
    if i > 0:
        fibonacci_list.append(i)
print(fibonacci_list)
######
fibonacci_list = []
i = 0
next_i = 0
last_i = 1
while i in range(0,35):
    
    i = next_i
    next_i = last_i
    last_i = i + next_i
    if i > 0:
        fibonacci_list.append(i)
print(fibonacci_list)

    
