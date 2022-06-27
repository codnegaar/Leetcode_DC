'''
Google_15_Leetcode_139_Word Break - Dynamic Programming.py
You are given a dictionary of words and a large input string. You have to find out whether the input string
can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.


Solution
Runtime complexity: O(2^N)
Space complexity: O(N^2)
 
This problem can be tackled by segmenting the input strign at every possible index to see if the string can be completely 
segmented into words in the dictionary. We can use an algorithm as follows:

'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            Dynamic Programming (DP) is an algorithmic technique for solving an optimization 
            problem by breaking it down into simpler subproblems and utilizing the fact that 
            the optimal solution to the overall problem depends upon the optimal solution to
            its subproblems.
        '''


        dp = [False] * (len(s) +1)
        
        dp[len(s)] = True
        
        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                
                if (i + len(word)) <= len(s) and s[i:  i+ len(word)] == word:
                    dp[i] = dp[i +len(word)]
                    
                if dp[i]:
                    break
        return dp[0]
      
      

'''

# Solution 2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        dp = [True] + [False] * len(s)        
        for i in range(1, len(s) + 1):            
            for word in wordDict:
                if dp[i - len(word)] and s[:i].endswith(word):
                    dp[i] = True
            
        return dp[-1]
        
 '''
			

        
