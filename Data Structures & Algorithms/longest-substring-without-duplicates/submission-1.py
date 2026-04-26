class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        result = 0
        l = 0

        for r in range(len(s)): 
            if s[r] in seen: 
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r  
            result = max(result, r-l+1)    
        return result