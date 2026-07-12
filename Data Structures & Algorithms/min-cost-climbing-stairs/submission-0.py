class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down1, down2 = 0,0 

        for i in range(2,len(cost) + 1):
            curr_cost = min(down1 + cost[i - 1], down2 + cost[i-2])

            down2 = down1
            down1 = curr_cost
            
        return down1
