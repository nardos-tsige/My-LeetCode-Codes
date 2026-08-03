class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')
        for num in nums:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            if digit_sum < min_sum:
                min_sum = digit_sum
        return min_sum
