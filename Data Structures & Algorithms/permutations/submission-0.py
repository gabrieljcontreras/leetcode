class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    def backtrack(self, nums, indx): 
        if indx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(indx, len(nums)):
            nums[indx], nums[i] = nums[i], nums[indx]
            self.backtrack(nums, indx + 1)
            nums[indx] , nums[i] = nums[i], nums[indx]