'''
Leetcode 763 Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. 
For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts. 

Example 1:
        Input: s = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
        Input: s = "eccbbbbdec"
        Output: [10]
 
Constraints:
        1 <= s.length <= 500
        s consists of lowercase English letters.
'''
class Solution(object):
    def partitionLabels(self, S):
        """
        Partition a string into as many parts as possible so that each letter appears in at most one part.
        
        Parameters:
        S (str): Input string of lowercase English letters
        
        Returns:
        List[int]: A list of integers representing the size of each partition
        """
        # Step 1: Record the last occurrence index for each character in the string
        last_occurrence = {char: idx for idx, char in enumerate(S)}
        
        # Step 2: Initialize pointers and result list
        end = 0       # The farthest index of the current partition
        start = 0     # The beginning index of the current partition
        result = []   # List to store the size of each partition
        
        # Step 3: Iterate through the string to create partitions
        for i, char in enumerate(S):
            # Update the 'end' to the farthest last occurrence seen so far
            end = max(end, last_occurrence[char])
            
            # If the current index reaches the 'end', we've found a complete partition
            if i == end:
                # Add the size of the partition to the result
                result.append(i - start + 1)
                # Move the start to the next index after the current partition
                start = i + 1
        
        return result

