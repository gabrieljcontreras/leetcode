class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        left, right = 0, len(height)-1
        maxRight, maxLeft = height[right], height[left]
        res = 0

        while left < right: 
            if maxLeft < maxRight: 
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
                
            else: 
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
        return res



