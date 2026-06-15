class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        res = []
        digit_map = {"2": "abc", "3" : "def", "4" : "ghi", "5": "jkl",
        "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"} #map of the digits values

        def dfs(start, path):
            if start == len(digits): #base case, we reach it we append to our res
                res.append(path)
                return 

            current_digit = digits[start] #our digit
            letters = digit_map[current_digit] #the letters of our digit
            
            for letter in letters: #iterate through letters
                dfs(start + 1, path + letter)  #append to our path for backtracking
        dfs(0, "")
        return res
                
                
