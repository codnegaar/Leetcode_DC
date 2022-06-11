class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0        
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            profit = max(profit,( prices[r] - prices[l]))
        return profit
