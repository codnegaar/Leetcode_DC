'''
Leetcode 39 Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40



'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(candidates, res, i, combination, s):
            if s == target:
                res.append(combination[:])
                return
            elif i == len(candidates) or s > target:
                return
            else:
                for n in range((target - s) // candidates[i]):
                    combination.append(candidates[i])
                    bt(candidates, res, i+1, combination, s + (n+1) * candidates[i])
                for n in range((target - s) // candidates[i]):
                    combination.pop()
                bt(candidates, res, i+1, combination, s)
                
        res = []
        bt(candidates, res, 0, [], 0)
        return res

# Second Solution
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates where the candidate numbers sum to target.
        
        Parameters:
        candidates (List[int]): List of positive integers to form combinations.
        target (int): Target sum for the combinations.
        
        Returns:
        List[List[int]]: List of all unique combinations that sum to target.
        """
        # Initialize result list to store valid combinations
        result = []

        def backtrack(start: int, combination: List[int], total: int):
            """
            Helper function to perform backtracking.

            Parameters:
            start (int): Current index in the candidates list.
            combination (List[int]): Current combination being built.
            total (int): Current sum of the combination.
            """
            # If the combination sums to target, add it to the result
            if total == target:
                result.append(combination[:])
                return

            # If the total exceeds target, stop exploring further
            if total > target:
                return

            # Explore further candidates starting from the current index
            for i in range(start, len(candidates)):
                # Add the current candidate to the combination
                combination.append(candidates[i])
                # Recursively call backtrack with updated total and combination
                backtrack(i, combination, total + candidates[i])
                # Remove the last added candidate to backtrack
                combination.pop()

        # Start the backtracking process from the first candidate
        backtrack(0, [], 0)
        return result

# Unit Tests
def test_combination_sum():
    solution = Solution()

    # Test Case 1
    candidates = [2, 3, 6, 7]
    target = 7
    assert sorted(solution.combinationSum(candidates, target)) == sorted([[2, 2, 3], [7]])

    # Test Case 2
    candidates = [2, 3, 5]
    target = 8
    assert sorted(solution.combinationSum(candidates, target)) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    # Test Case 3
    candidates = [2]
    target = 1
    assert solution.combinationSum(candidates, target) == []

    # Test Case 4
    candidates = [1]
    target = 2
    assert solution.combinationSum(candidates, target) == [[1, 1]]


    print("All test cases passed!")

# Run the tests
test_combination_sum()

       
