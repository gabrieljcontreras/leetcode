class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right: 
            cursum = numbers[left] + numbers[right]

            if cursum > target: 
                right -= 1
            elif cursum < target: 
                left += 1
            else: 
                return [left+1, right+1]
        return []