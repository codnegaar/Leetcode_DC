'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        https://docs.python.org/3/library/collections.html    
        
        class collections.Counter([iterable-or-mapping])
        
        A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary
        keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or 
        negative counts. The Counter class is similar to bags or multisets in other languages.
        Elements are counted from an iterable or initialized from another mapping (or counter):
        '''
        
        alphabets = collections.Counter(s);
        
        for index in range(len(s)):
            if alphabets[s[index]] == 1:
                return index
        return -1
      
      
