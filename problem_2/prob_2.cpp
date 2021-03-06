/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 2:
        Each new term in the Fibonacci sequence is generate by adding the previous two terms. 
        By Starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 44, 89,...

        By considering the terms in the fibonacci sequence whose values do not exceed four million, 
        find the sum of the even valued terms.


    Solution & Thinking:
        - We're looking for a sum of numbers, so a variable is needed to store this su,/
        - we're looking to output the sum, so finish with a return or print
        - We're looking for terms in the fibonacci sequence below 4 million, so that would be an upper limit condition
        - if number is even i.e. n modulo 2 = 0, add to sum total
        - Continue calculating the fibonacci sequence until the upper limit
*/

#include <iostream>

using namespace std;

int main (int argc, char **argv)
{
    int sum = 0;

    int n1 = 0;
    int n2 = 1;
    int prev_n1=0;

    while (n1 <= 4000000)
    {
        if(n1 % 2 == 0){
            sum += n1;
        }
        prev_n1 = n1;
        n1 = n2;
        n2 = prev_n1+n2;
    }

    cout << "The sum of the even valued fibonacci terms below 4 millions is " <<  sum << "." << endl;
}