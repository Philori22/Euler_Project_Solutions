#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 3:
        The prime factors of 13195 are 5, 7 , 13, 29.
        What is the largest prime factor of the number 600851475143?


    Solution & Thinking:
        - TO-DO
'''

import math

# Define max prime factor function
def maxPrimeFactor(n):
    while n % 2 ==0:
        max_prime = 2
        n /= 1

    for i in range(3,int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
        max_Prime = i
        n = n / i

    if n > 2:
        max_Prime = n
    return int(max_Prime)


def main():

    n = 600851475143
    print(maxPrimeFactor(n))


if __name__ == "__main__":
    main()




