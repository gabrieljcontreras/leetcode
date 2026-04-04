class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dicty = {}
        for char in s: 
            if char not in dicty:
                dicty.update({char: 1})
            elif char in dicty: 
                dicty.update({char: dicty[char] + 1})

        for char in t:
            if char in dicty: 
                dicty.update({char: dicty[char] - 1})
            else:
                return False

        for val in dicty.values():
            if val != 0:
                return False
        return True