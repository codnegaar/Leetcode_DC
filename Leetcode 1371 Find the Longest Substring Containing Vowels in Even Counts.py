'''

Leetcode 1371 Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
 
Example 1:
        Input: s = "eleetminicoworoep"
        Output: 13
        Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
        
Example 2:
        Input: s = "leetcodeisgreat"
        Output: 5
        Explanation: The longest substring is "leetc" which contains two e's.
        
Example 3:
        Input: s = "bcbcbc"
        Output: 6
        Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 
Constraints:
        1 <= s.length <= 5 x 10^5
        s contains only lowercase English letters.

'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state_map = {0: -1}
        max_len, mask = 0, 0

        for i, char in enumerate(s):
            if char in vowels:
                mask ^= vowels[char]
            if mask in state_map:
                max_len = max(max_len, i - state_map[mask])
            else:
                state_map[mask] = i

        return max_len



# Solution II
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        mask = 0
        max_len = 0
        mask_map = {0: -1}  # Map of mask to index, initialized with mask 0 at index -1

        for i, char in enumerate(s):
            if char in vowel_to_bit:
                mask ^= vowel_to_bit[char]  # Flip the bit corresponding to the vowel

            if mask in mask_map:
                # If this mask was seen before, calculate the length of the substring
                max_len = max(max_len, i - mask_map[mask])
            else:
                # If this is the first time we see this mask, store its index
                mask_map[mask] = i

        return max_len
