class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) -1
        while l < r: 
            count = 0
            m = (l + r) //2 

            for num in range(len(nums)): 
                if nums[num] <= m: 
                    count +=1 

            if count > m: 
                r = m
            else: 
                l = m + 1
        return l