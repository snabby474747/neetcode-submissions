class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float("inf")
        n = len(prices)

        for i in range (0,n):
            min_profit = min(min_profit,prices[i])
            max_profit =  max(max_profit,prices[i]-min_profit)

        return max_profit
