# encoding:UTF-8
'''
Fibonacci series is one in which a new number is 
generated by adding the previous two numbers. 
Eg : 0 1 1 2 3 5 8 13 21 34 55 89
Algorithm for finding Fibonacci number less than a certain number n
Take base case f = 0 and l = 1. Then t = f + l is the new number.
Then replace the first number f = l and l = t. Perform this operation 
recursively.
'''

# f is the first number, l is the second number and n is the upper limit
# of the series
def fibonacci(f, l, n):
    t = f + l
    if (t < n):
        print(t)
        return fibonacci(l, t, n)
    else:
        return t

n = int(input("Enter the upper limit of the series : "))
fibonacci(0, 1, n)