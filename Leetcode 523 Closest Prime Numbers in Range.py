'''
Leetcode 523 Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:
left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:
          Input: left = 10, right = 19
          Output: [11,13]
          Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
          The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
          Since 11 is smaller than 17, we return the first pair.

Example 2:
        Input: left = 4, right = 6
        Output: [-1,-1]
        Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
         

Constraints:
        1 <= left <= right <= 106

'''

from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        Finds the pair of closest prime numbers within the given range [left, right].
        
        Parameters:
        left (int): The lower bound of the range.
        right (int): The upper bound of the range.

        Returns:
        List[int]: A list containing two closest prime numbers. 
                   If no such pair exists, returns [-1, -1].
        """
        if right - left < 1:
            return [-1, -1]  # No valid range for a pair of primes
        
        # Ensure left is at least 2 (smallest prime)
        left = max(2, left)

        # Use the Sieve of Eratosthenes to find primes up to `right`
        primes = self.sieve_of_eratosthenes(right)

        # Filter primes within the given range
        primes_in_range = [p for p in primes if p >= left]

        # If there are fewer than two primes, return [-1, -1]
        if len(primes_in_range) < 2:
            return [-1, -1]

        # Find the closest pair
        min_diff = float('inf')
        res = [-1, -1]
        for i in range(len(primes_in_range) - 1):
            diff = primes_in_range[i + 1] - primes_in_range[i]
            if diff < min_diff:
                min_diff = diff
                res = [primes_in_range[i], primes_in_range[i + 1]]
                if diff == 2:  # The closest prime pair possible
                    return res

        return res

    def sieve_of_eratosthenes(self, n: int) -> List[int]:
        """
        Implements the Sieve of Eratosthenes algorithm to find all prime numbers up to `n`.

        Parameters:
        n (int): The upper limit for prime numbers.

        Returns:
        List[int]: A list of prime numbers up to `n`.
        """
        if n < 2:
            return []

        is_prime = [True] * (n + 1)  # Boolean array to mark primes
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:  # If `i` is prime, mark its multiples as non-prime
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False

        return [i for i in range(n + 1) if is_prime[i]]
