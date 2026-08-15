class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #This is the best solution to this problem. Make sure to know the XOR operator for python 
        res = 0
        for i in nums: 
            res = i ^ res
        return res