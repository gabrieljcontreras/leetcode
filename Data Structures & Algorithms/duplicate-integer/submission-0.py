class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there = set()
        for n in nums: 
            if n in there: 
                return True
            there.add(n)
        return False