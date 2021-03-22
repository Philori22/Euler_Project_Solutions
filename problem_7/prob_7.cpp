/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 7:
        By listing the first 6 numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10001st prime number?

    Solution & Thinking:
        - TO-DO
*/

#include <iostream>

using namespace std;


bool is_prime(int n)
{
    int factor = 2;
    while (factor * factor <= n){
        if ( n% factor == 0)
        {
            return 0;
        }
        factor +=1;
    }


    return 1;
}



int nth_prime_number(int n)
{
    if (n ==1)
    {
        return 2;
    }
    int count = 1;
    int num = 1;
    while (count < n)
    {
        num+=2;
        if (is_prime(num))
        {
            count +=1;
        }
    }

    return num;
}


int main (int argc, char **argv)
{

    cout << "Answer is: " << nth_prime_number(10001) << endl;
}