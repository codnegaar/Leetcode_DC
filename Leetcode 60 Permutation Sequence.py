'''


60. Permutation Sequence
 
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence. 

Example 1:
        Input: n = 3, k = 3
        Output: "213"

Example 2:
        Input: n = 4, k = 9
        Output: "2314"

Example 3:
        Input: n = 3, k = 1
        Output: "123"

Constraints:
        1 <= n <= 9
        1 <= k <= n!

'''
class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    ans = ''
    nums = [i + 1 for i in range(n)]
    fact = [1] * (n + 1)  # fact[i] := i!

    for i in range(2, n + 1):
      fact[i] = fact[i - 1] * i

    k -= 1  # 0-indexed

    for i in reversed(range(n)):
      j = k // fact[i]
      k %= fact[i]
      ans += str(nums[j])
      nums.pop(j)

    return ans
