class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0,0 

        for i in nums:
            money = max(house1, house2 + i)

            house2 = house1
            house1 = money

        return money