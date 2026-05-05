class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        best = r
        while l <= r: 
            m = (l+r)//2
            
            total = sum((p + m - 1) // m for p in piles)
            
            if total > h: 
                l = m+1

            elif total <= h:
                best = m
                r = m -1
        return best