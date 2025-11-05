'''
Leetcode 3321 Find X-Sum of All K-Long Subarrays II
 
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].

Example 1:
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]
Explanation:
        For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
        For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
        For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

Example 2:
Input: nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]
Explanation: Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

Constraints:
        nums.length == n
        1 <= n <= 105
        1 <= nums[i] <= 109
        1 <= x <= k <= nums.length
'''

class Solution:
    def findXSum(self, nums: List[int], k: int, m: int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        seen, selected = set(), set()
        curr, rem = [], []
        sm = 0

        def neg_tup(tup):
            return -tup[0], -tup[1]

        def take(x):
            if cnt[x] > 0 and x in selected:
                nonlocal sm
                selected.remove(x)
                sm -= cnt[x] * x

        def update_lazy():
            while curr:
                c, x = curr[0]
                if x in selected and cnt[x] == c:
                    break
                heappop(curr)

            while rem:
                c, x = neg_tup(rem[0])
                if x not in selected and cnt[x] == c:
                    break
                heappop(rem)

            return bool(rem)

        ans = []
        for i in range(n):
            take(nums[i])
            cnt[nums[i]] += 1
            seen.add(nums[i])
            heappush(rem, (-cnt[nums[i]], -nums[i]))

            if i >= k:
                j = i - k
                take(nums[j])
                cnt[nums[j]] -= 1
                if cnt[nums[j]] > 0:
                    heappush(rem, (-cnt[nums[j]], -nums[j]))

            while update_lazy() and (len(selected) < m or neg_tup(rem[0]) > curr[0]):
                t = neg_tup(heappop(rem))
                heappush(curr, t)
                selected.add(t[1])
                sm += t[0] * t[1]
                if len(selected) > m:
                    t = heappop(curr)
                    heappush(rem, neg_tup(t))
                    selected.remove(t[1])
                    sm -= t[0] * t[1]

            if i + 1 >= k:
                ans.append(sm)

        return ans
