class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for num in range(len(nums)- 2, -1, -1): 
            if num + nums[num] >= goal: 
                goal = num
        return goal == 0