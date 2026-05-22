class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0

        for price in prices:
            profit = price - min_price
            max_price = max(max_price, profit)

            min_price= min(min_price, price)
        return max_price