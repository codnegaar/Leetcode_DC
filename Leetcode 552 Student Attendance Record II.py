'''
Leetcode 552 Student Attendance Record II

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. 
The record only contains the following three characters:

        'A': Absent.
        'L': Late.
        'P': Present.
        Any student is eligible for an attendance award if they meet both of the following criteria:
                The student was absent ('A') for strictly fewer than 2 days total.
                The student was never late ('L') for 3 or more consecutive days.
                Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award.
                The answer may be very large, so return it modulo 109 + 7.

Example 1:
        Input: n = 2
        Output: 8
        Explanation: There are 8 records with length 2 that are eligible for an award:
        "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
        Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:
        Input: n = 1
        Output: 3

Example 3:
        Input: n = 10101
        Output: 183236316
 

Constraints:
        1 <= n <= 105

'''


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Memoization cache to avoid recalculating states
        # Cache structured as [current_index][count_of_A's][consecutive_L's]
        cache = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        def count_valid_records(index: int, a_count: int, l_count: int) -> int:
            # Base case: if we have filled all positions, return 1 valid record
            if index == n:
                return 1
            
            # If this state has been calculated before, return the cached result
            if cache[index][a_count][l_count] != -1:
                return cache[index][a_count][l_count]
            
            # Start counting valid records from this state
            result = 0
            
            # Place 'P': Always possible
            result = count_valid_records(index + 1, a_count, 0) % MOD
            
            # Place 'A': Only if we haven't placed an 'A' before (a_count < 1)
            if a_count < 1:
                result = (result + count_valid_records(index + 1, a_count + 1, 0)) % MOD
            
            # Place 'L': Only if there are less than 2 consecutive 'L's
            if l_count < 2:
                result = (result + count_valid_records(index + 1, a_count, l_count + 1)) % MOD
            
            # Save in cache
            cache[index][a_count][l_count] = result
            return result
        
        return count_valid_records(0, 0, 0)

# Example of using the class
sol = Solution()
print(sol.checkRecord(2))  # Example to compute number of valid records for n=2
