# https://www.cs.cornell.edu/courses/cs2110/2014fa/L07-Recursion/recursion_practice.pdf

# 1. Compute the Factorial of a number N. F act(N) = N × (N −1)· · · 1.
def factorial(n):
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1)
# 2. Compute the sum of natural numbers until N.
def sum(n):
    if n == 1: 
        return 1
    return n + sum(n-1)

# 3. Write a function for mutliply(a, b), where a and b are both positive 
# integers, but you can only use the + or − operators.
def multiply(a, b):
    if b == 1:
        return a
    return a + multiply(a, b-1)
# 4. In the lecture, we discussed a method to raise a double to an
# integer power. In this question, write a recursive function that
# allows raising to a negative integer power as well.
def power(x, n):
    # Base case
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1 / x
    
    # Recursive case
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    elif n > 0:
        return half * half * x
    else:
        return half * half / x
# 5. Find Greatest Common Divisor (GCD) of 2 numbers using recursion.
def gcd(a, b):
    # Base case
    if b == 0:
        return a
    # Recursive case
    return gcd(b, a % b)
# 6. Write a recursive function to reverse a string. Write a recursive 
# function to reverse the words in a string, i.e., ”cat is running”
# becomes ”running is cat”.
def reverse_words(s):
    # Base case
    if len(s.split()) == 1:
        return s
    
    # Recursive case
    return s.split()[-1] + " " + reverse_words(" ".join(s.split()[:-1]))
