/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 4:
        A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009= 91 x 99.

        Find the largest palindrome made from the product of two three digit numbers


    Solution & Thinking:
        - TO-DO
*/

#include "../0-include/range.hpp" // python like for loop
#include <iostream>
#include <string>
#include <algorithm> // added for reversing string

using namespace std;
using namespace util;
using namespace lang;

int x;
string s;

int main(int argc, char **argv)
{
    int n = 0;
    for (auto a : range(999, 1).step(-1))
    {
        for(auto b : range(a, 1).step(-1))
        {
            x = a*b;
            if (x > n)
            {
                s = to_string(a * b);

                string s_rev(s);
                reverse(s_rev.begin(), s_rev.end());

                if (s == s_rev)
                {
                    n = a * b;
                }
            
            }
        }
    }

    cout << "The largest palindrome number from the product of two three digit numbers is " << n << "." << endl;

}