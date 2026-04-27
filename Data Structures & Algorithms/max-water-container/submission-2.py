class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        res = 0
        while left < right: 
            res = max(res, (right - left) * min(heights[right], heights[left]))
            if heights[left] < heights[right]: 
                left += 1
            elif heights[left] > heights[right]:
                    right -=1
            else: 
                right -=1 
        return res 

        
