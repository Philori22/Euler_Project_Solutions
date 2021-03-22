#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 6:
        The sum of the squares of the first ten natural numbers is 385 The square of the sum of the first ten natural numbers is 3025
    hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
    Find the difference between the sum of the squares of the first hundred numbers and the square of the sum.

    Solution & Thinking:
        - TO-DO
'''


def sumOfSquares(x):
  sum_of_squares = 0
  for i in range(101):
    sum_of_squares += i*i
  return sum_of_squares


def squareofSum(x):
  square_of_sum = 0

  for i in range(101):
    square_of_sum += i
  square_of_sum = square_of_sum * square_of_sum  
  return square_of_sum
  

def ssd(x): return squareofSum(x) - sumOfSquares(x)

def main():
    print(ssd(100))

if __name__ == "__main__":
    main()