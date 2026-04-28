class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = 0 
        length = len(s1)

        while r < len(s2): 
            if sorted(s2[r:r+length]) == sorted(s1): 
                return True 
                
            r += 1
        return False


