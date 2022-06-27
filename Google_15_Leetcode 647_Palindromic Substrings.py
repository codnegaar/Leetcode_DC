'''

Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
          Input: s = "abc"
          Output: 3
          Explanation: Three palindromic strings: "a", "b", "c".


Example 2:
          Input: s = "aaa"
          Output: 6
          Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"


Solution:

          Runtime complexity: O(N^2)
          Space complexity: O(1)

          We will iterate through each letter in the input string. For each letter, we can find palindromes by expanding to the left and 
          right will we check for even and odd length palindromes. If there are no palindromes, move to the next letter. We find palindromes 
          by checking if the left and right character are equal. If they are, we print out the palindrome substring.

'''


