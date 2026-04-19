class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_price = 0
        lowest_price = prices[0]
        for sell in prices: 
            highest_price = max(highest_price, sell - lowest_price)
            lowest_price = min(lowest_price, sell)
        return highest_price