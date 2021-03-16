#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 1:
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we gat 3,5,6 and 9. 
        The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000

    Solution & Thinking:
        - we're looking for a sum of numbers, so a variable is needed to store this sum.
        - Looking at all multiples below 1000. there fore ranging rom 0 - 1000.
        - Looking for multiples of 3 or 5 to as to sum total.
            -When one number can be divided by another number with no remainder, we can say the 
            first number is divisible by the other number. i.e. a multiple of it too
            - Modulo Arithmetic - The modulo operation '%' is the remainder when dividing.
            - If given number modulo 5 is 0, then we add it, else we move to the next number in range
        - If it is a multiple, add to the sum total.
'''


def main():
    sum = 0
    for num in range(0,1000):
        if num % 5 == 0 or num % 3 == 0:
            sum +=num

    print('answer: ', sum)


if __name__ == "__main__":
    main()