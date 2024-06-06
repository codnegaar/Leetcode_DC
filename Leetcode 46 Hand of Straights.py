'''
Leetcode 46 Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
        Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
        Output: true
        Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
        Input: hand = [1,2,3,4,5], groupSize = 4
        Output: false
        Explanation: Alice's hand can not be rearranged into groups of 4.    
         
Constraints:
        1 <= hand.length <= 104
        0 <= hand[i] <= 109
        1 <= groupSize <= hand.length

'''

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by the group size
        if len(hand) % groupSize != 0:
            return False
        
        # Count the occurrences of each card
        count = Counter(hand)
        
        # Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        # Try to form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # Only consider if there are cards of this value left
                start_count = count[key]
                # Check if we can form a group starting from the current card value
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        
        # If we successfully form all groups, return True
        return True


