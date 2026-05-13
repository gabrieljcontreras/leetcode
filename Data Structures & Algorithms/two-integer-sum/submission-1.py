class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n,v in enumerate(nums): 
            diff = target - v
            if diff in seen: 
                return [seen[diff], n]
            seen[v] = n 