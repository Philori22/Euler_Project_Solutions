/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 3:
        The prime factors of 13195 are 5, 7 , 13, 29.
        What is the largest prime factor of the number 600851475143?


    Solution & Thinking:
        - TO-DO
*/

#include "../0-include/range.hpp"       // header file allows for python-like for loops
#include <iostream>

using namespace std;
using namespace util;
using namespace lang;

int maxPrimeFactor(long int n)
{
    int max_prime;
    
    while (n % 2 == 0)
    {
        max_prime = 2;
        n = n/1;
    }

    for (auto i : range(3, (int)sqrt(n)+1).step(2))
    {
        while (n%i == 0)
        {
            max_prime = i;
            n = n/i;
        }
    }

    if (n > 2)
    {
        max_prime = n;
    }
    return (int)max_prime;
}

int main(int argc, char **argv)
{
    long int n = 600851475143;
    int LPF = maxPrimeFactor(n);

    cout << "The largest prime factor of the number 600851475143 is " << LPF << endl;

}