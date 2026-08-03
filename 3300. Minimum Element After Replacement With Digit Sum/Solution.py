class Solution:
    def minElement(self, nums: List[int]) -> int:
            return min(sum(int(digit) for digit in str(num)) for num in nums)
