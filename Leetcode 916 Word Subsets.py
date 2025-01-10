'''
Leetcode 916 Word Subsets

You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order. 

Example 1:
        Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
        Output: ["facebook","google","leetcode"]

Example 2:
        Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
        Output: ["apple","google","leetcode"] 

Constraints:
        1 <= words1.length, words2.length <= 104
        1 <= words1[i].length, words2[i].length <= 10
        words1[i] and words2[i] consist only of lowercase English letters.
        All the strings of words1 are unique.

'''
from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Compute maximum character frequencies required across words2
        maxCharFreq = Counter()
        for word in words2:
            wordFreq = Counter(word)
            for ch in wordFreq:
                maxCharFreq[ch] = max(maxCharFreq[ch], wordFreq[ch])

        # Find all universal words in words1
        universalWords = []
        for word in words1:
            wordFreq = Counter(word)
            if all(wordFreq[ch] >= maxCharFreq[ch] for ch in maxCharFreq):
                universalWords.append(word)

        return universalWords
