class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        hold = -prices[0]
        sold = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_free = free

            
            hold = max(prev_hold, prev_free -price)
            sold = prev_hold + price
            free = max(prev_free, prev_sold)

        
        return max(sold, free)