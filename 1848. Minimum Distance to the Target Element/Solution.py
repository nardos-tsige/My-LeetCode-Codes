class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                distance = abs(i - start)
                min_distance = min(min_distance, distance)
        
        return min_distance
