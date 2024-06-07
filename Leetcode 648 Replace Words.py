'''

Leetcode 648 Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with
the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.

Example 1:        
        Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
        Output: "the cat was rat by the bat"
        
Example 2:
        Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
        Output: "a a b c"
 

Constraints:
        1 <= dictionary.length <= 1000
        1 <= dictionary[i].length <= 100
        dictionary[i] consists of only lower-case letters.
        1 <= sentence.length <= 106
        sentence consists of only lower-case letters and spaces.
        The number of words in sentence is in the range [1, 1000]
        The length of each word in sentence is in the range [1, 1000]
        Every two consecutive words in sentence will be separated by exactly one space.
        sentence does not have leading or trailing spaces.

'''

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.endOfWord = True

    def getRoot(self, word: str) -> str:
        curr = self.root
        prefix = []
        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
            prefix.append(c)
            if curr.endOfWord:
                return ''.join(prefix)
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.addWord(word)

        words = sentence.split()
        replaced_words = [self.getRoot(word) for word in words]

        return ' '.join(replaced_words)
