class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        min_val = min(nums)
        max_val = max(nums)
        nums_set = set(nums)
        missing = []
        for num in range(min_val, max_val + 1):
            if num not in nums_set:
                missing.append(num)
    
        return missing
