class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        #case 1: three largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
        #case 2: two smallest(most negative) and the largest
        case2 = nums[0] * nums[1] * nums[-1]
        return max(case1, case2)
