#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 4:
        A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009= 91 x 99

        Find the largest palindrome made from the product of two three digit numbers


    Solution & Thinking:
        - TO-DO
'''

def main():
    n = 0
    for a in range(999,1,-1):
        for b in range(a,1,-1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b
    print(n)

if __name__ == "__main__":
    main()