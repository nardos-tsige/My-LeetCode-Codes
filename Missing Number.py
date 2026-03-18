# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)+1):
#             if i not in nums:
#                 return i

# optimized 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # taking the sum of expected outcome numbers form 0 - n and subtracting what's actually found inside an array
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
