class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0
        for i in range(len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                res += prices[i] - min_price
                min_price = prices[i]
        return res