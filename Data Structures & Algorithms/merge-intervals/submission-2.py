class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ This solution is far better than the last, it utilizes
        the interval pattern in a much easier way to read/ implement, follow
        this one"""
        
        intervals.sort()
        res = []
        for start, end in intervals: 
            if not res: 
                res.append([start, end])
            else:
                if start <= res[-1][1]: 
                    res[-1][1] = max(res[-1][1], end)
                else: 
                    res.append([start, end])
        return res