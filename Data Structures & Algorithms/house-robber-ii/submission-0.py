class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        def rob(houses):
            house1 = 0
            house2 = 0
            for i in houses: 
                money = max(house1, house2 +i)
                house2 = house1
                house1 = money
            return house1
        
        scenario1 = rob(nums[:-1])
        scenario2 = rob(nums[1:])

        return max(scenario1, scenario2)