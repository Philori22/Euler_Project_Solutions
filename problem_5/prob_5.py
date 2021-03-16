#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 5:
        2520 is the smallest number tha can be divided by each of the numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?


    Solution & Thinking:
        - TO-DO
'''


def gcd(x,y): 
    return y and gcd(y, x % y) or x

def lcm(x,y): 
    return x * y / gcd(x,y)


def main():
    # smallest positive number that is evently divisible by all the numbers from 1 to 20

    n = 1
    for i in range(1,21):
        n = lcm(n, i)
    print("The answer is %s" % (n))

if __name__ == "__main__":
    main()