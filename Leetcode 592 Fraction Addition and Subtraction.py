'''
Leetcode 592 Fraction Addition and Subtraction

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1. 

Example 1:
        Input: expression = "-1/2+1/2"
        Output: "0/1"

Example 2:
        Input: expression = "-1/2+1/2+1/3"
        Output: "1/3"

Example 3:
        Input: expression = "1/3-1/2"
        Output: "-1/6"
 
Constraints:
        The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
        Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
        The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. 
        If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
        The number of given fractions will be in the range [1, 10].
        The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

'''

import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Extracting all integers (both numerators and denominators) from the expression
        fractions = list(map(int, re.findall(r'[+-]?\d+', expression)))
        
        # Initial numerator and denominator values for the result
        result_numerator = 0
        result_denominator = 1
        
        # Iterating through the extracted numbers, where each fraction is represented by two numbers
        for i in range(0, len(fractions), 2):
            current_numerator = fractions[i]
            current_denominator = fractions[i + 1]
            
            # Updating the result fraction using the formula: 
            # a/b + c/d = (a*d + b*c) / (b*d)
            result_numerator = result_numerator * current_denominator + current_numerator * result_denominator
            result_denominator *= current_denominator
        
        # Simplify the resulting fraction by dividing by the greatest common divisor (GCD)
        common_divisor = gcd(result_numerator, result_denominator)
        simplified_numerator = result_numerator // common_divisor
        simplified_denominator = result_denominator // common_divisor
        
        # Returning the result as a string in "numerator/denominator" format
        return f"{simplified_numerator}/{simplified_denominator}"
