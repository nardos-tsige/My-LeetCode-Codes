class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        return next(i for i in range(1, len(nums)+2) if i not in s)
