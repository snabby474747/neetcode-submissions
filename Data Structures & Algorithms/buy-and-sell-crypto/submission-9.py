class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min_prices = float("inf")
        # n = len(prices)

        # for i in range (0,n):
        #     min_prices = min(min_prices,prices[i])
        #     max_profit =  max(max_profit,prices[i]-min_prices)

        # return max_profit

        max_profit = 0
        min_pri = float("inf")
        n = len(prices)

        for i in range(0,n):
            min_pri = min(min_pri,prices[i])
            max_profit = max(max_profit,prices[i]-min_pri)

        return max_profit