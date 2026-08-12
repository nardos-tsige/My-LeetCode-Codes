class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1
        
        prefix_sum = sum(nums[:i + 1])
        num_set = set(nums)
        
        x = prefix_sum
        while x in num_set:
            x += 1
        
        return x
