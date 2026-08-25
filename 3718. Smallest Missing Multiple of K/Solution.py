class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        i = k
        while i in s: i += k
        return i
