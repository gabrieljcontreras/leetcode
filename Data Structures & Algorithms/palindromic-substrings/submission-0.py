class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: 
            return 0 

        total = 0
        start, end = 0,0

        def expansion(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            total += expansion(i,i)
            total += expansion(i,i+1)

        return total


            