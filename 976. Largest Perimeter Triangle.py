class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            #triangle inequality:- a + b > c(with a ≥ b ≥ c)
            #since array is sorted descending we check if nums[i+1] + nums[i+2] > nums[i]
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0
