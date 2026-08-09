class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        rightmax = -1
        
        for i in range(len(arr)-1, -1, -1): 
            res[i] = rightmax
            rightmax = max(arr[i], rightmax)
        return res
