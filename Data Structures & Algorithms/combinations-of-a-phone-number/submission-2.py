class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        res = []
        digit_map = {"2": "abc", "3" : "def", "4" : "ghi", "5": "jkl",
        "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"} 

        def dfs(start, path):
            if start == len(digits): 
                res.append(path)
                return 

            current_digit = digits[start] 
        
            
            for letter in digit_map[current_digit] : 
                dfs(start + 1, path + letter)  
        dfs(0, "")
        return res
                
                
