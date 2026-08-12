class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        age = []
        for i in details: 
            if int(i[11:13]) > 60: 
                res+=1 
        return res
                
        