'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = collections.defaultdict(list)

    for str in strs:
      key = ''.join(sorted(str))
      dict[key].append(str)

    return dict.values()


# Second solution

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26  # Frequency array for 'a' to 'z'
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            print(f"String: {s}, Key: {key}")  # Debug: Check string and its key
            anagrams_dict[key].append(s)
        
        # Debug: Check dictionary contents
        print(f"Anagrams Dictionary: {dict(anagrams_dict)}")
        return list(anagrams_dict.values())  # Ensure output is List[List[str]]

# Test Cases
solution = Solution()
test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],  # Edge case: single empty string
    ["a"],  # Edge case: single character
    [],  # Edge case: empty input
    ["abc", "bca", "cab", "xyz", "yxz"]  # Anagrams and non-anagrams
]

for i, test in enumerate(test_cases, 1):
    print(f"\nTest Case {i}: {test}")
    result = solution.groupAnagrams(test)
    print(f"Result: {result}")

