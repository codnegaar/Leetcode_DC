'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long 
sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        l = len(s)
        dic = {}
        DNALST = []
        
        for i in range(l):
            DNA = s[i:i+10]
            dic [DNA] = dic.get(DNA,0) + 1
            
        for key, value in dic.items():
            if value > 1:
                DNALST.append(key)
                
        return DNALST
