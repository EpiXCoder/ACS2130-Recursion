# https://www.cs.cornell.edu/courses/cs2110/2014fa/L07-Recursion/recursion_practice.pdf

# 1. Compute the Factorial of a number N. F act(N) = N × (N −1)· · · 1.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
# 2. Compute the sum of natural numbers until N.
# 3. Write a function for mutliply(a, b), where a and b are both positive
# integers, but you can only use the + or − operators.
# 4. In the lecture, we discussed a method to raise a double to an
# integer power. In this question, write a recursive function that
# allows raising to a negative integer power as well.
# 5. Find Greatest Common Divisor (GCD) of 2 numbers using recursion.
# 6. Write a recursive function to reverse a string. Write a recursive
# function to reverse the words in a string, i.e., ”cat is running”
# becomes ”running is cat”.