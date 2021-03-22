/*
    C++ IMPLEMENTATION
    -------------------------------------------------------------------------------------------------
    Problem 6:
        The sum of the squares of the first ten natural numbers is 385 The square of the sum of the first ten natural numbers is 3025
    hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
    Find the difference between the sum of the squares of the first hundred numbers and the square of the sum.

    Solution & Thinking:
        - TO-DO
*/


#include <iostream>
#include "../0-include/range.hpp"

using namespace std;
using namespace util;
using namespace lang;

// Sum of Squares
int sumOfSquares(int x)
{
    int sum_of_squares = 0;

    for(auto i: range(0,101)){
        sum_of_squares += i*i;
    }
    return sum_of_squares;
}

// Square of sum
int squareofSum(int x){
    int square_of_sum = 0;

    for (auto i: range(0,101)){
        square_of_sum += i;
    }
    square_of_sum = square_of_sum * square_of_sum;

    return square_of_sum;
}

// difference
int ssd(int x){ return squareofSum(x) - sumOfSquares(x);}


int main(int argc, char **argv)
{
    cout << "answer is " << ssd(100) << endl;

}