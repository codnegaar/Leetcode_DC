'''

Leetcode 857 Minimum Cost to Hire K Workers
 
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.
We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
Every worker in the paid group must be paid at least their minimum wage expectation.
In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must 
be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:
        Input: quality = [10,20,5], wage = [70,50,30], k = 2
        Output: 105.00000
        Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
        
Example 2:
        Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
        Output: 30.66667
        Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
 
Constraints:
        n == quality.length == wage.length
        1 <= k <= n <= 104
        1 <= quality[i], wage[i] <= 104

'''


import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate the wage to quality ratio and pair it with quality
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        
        # Initialize variables
        max_heap = []
        quality_sum = 0
        res = float('inf')  # Start with infinity to find minimum
        
        # Build the initial heap and quality sum for the first 'k' workers
        for ratio, qual in workers[:k]:
            heapq.heappush(max_heap, -qual)  # Use negative to create a max heap
            quality_sum += qual
        
        # Calculate the cost with the initial group of 'k' workers
        max_ratio = workers[k-1][0]  # The k-th smallest ratio defines the first viable group
        res = max_ratio * quality_sum
        
        # Process the rest of the workers
        for ratio, qual in workers[k:]:
            # Pop the largest quality worker and push the new one
            quality_sum += qual + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -qual)
            
            # Update the result if the new group has a lower cost
            res = min(res, ratio * quality_sum)
        
        return res

# Example usage:
sol = Solution()
print(sol.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))  # Example call
