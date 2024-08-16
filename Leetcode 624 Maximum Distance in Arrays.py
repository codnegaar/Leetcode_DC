'''
Leetcode 624 Maximum Distance in Arrays

You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance 
between two integers a and b to be their absolute difference |a - b|. Return the maximum distance.

Example 1:
        Input: arrays = [[1,2,3],[4,5],[1,2,3]]
        Output: 4
        Explanation: One way to reach the maximum distance of 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:
        Input: arrays = [[1],[1]]
        Output: 0
 

Constraints:        
        m == arrays.length
        2 <= m <= 105
        1 <= arrays[i].length <= 500
        -104 <= arrays[i][j] <= 104
        arrays[i] is sorted in ascending order.
        There will be at most 105 integers in all the arrays.

'''
class Solution(object):
    def maxDistance(self, arrays):
        # Initialize smallest and biggest with the first array's first and last elements
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        # Iterate over the arrays starting from the second array
        for arr in arrays[1:]:
            # Calculate possible maximum distances and update max_distance
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))

            # Update smallest and biggest for future comparisons
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
