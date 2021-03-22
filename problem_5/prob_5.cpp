/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 5:
        2520 is the smallest number tha can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

    Solution & Thinking:
        - TO-DO
*/


#include <iostream>
#include "../0-include/range.hpp"

using namespace std;
using namespace util;
using namespace lang;



// Euclidean GCD recursive funcrion
int gcd(int x, int y)
{
    if (y == 0)
        return x;
    return gcd(y, x%y);
}

// Euclidean Least Common multiple
int lcm(int x, int y)
{
    return x * y / gcd(x,y);
}


int main(int argc, char **argv)
{
    int n = 1;

    for (auto i : range(1,20)) 

    {
        n = lcm(n, i);
    }

    cout << "The answer is " << n << endl;

}