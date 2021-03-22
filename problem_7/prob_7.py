#!/usr/bin/env python
'''
    PYTHON IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 7:
        By listing the first 6 numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10001st prime number?

    Solution & Thinking:
        - TO-DO
'''


def is_prime(n):
  factor = 2
  while (factor * factor <=  n):
    if n % factor == 0:
      return False
    factor +=1
  return True
  

def nth_prime_number(n):
  if n == 1:
    return 2
  count = 1
  num = 1
  while(count < n):
    num +=2
    if is_prime(num):
      count +=1
  return num


def main():
    print(nth_prime_number(10001))

if __name__ == "__main__":
    main()