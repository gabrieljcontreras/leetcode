class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        global_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            old_max = curr_max

            curr_max = max(num, old_max * num, curr_min * num)
            curr_min = min(num, old_max * num, curr_min * num)

            global_max = max(global_max, curr_max)
            
        return global_max