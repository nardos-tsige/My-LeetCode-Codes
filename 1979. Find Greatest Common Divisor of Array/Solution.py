class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        
        return math.gcd(min_num, max_num)
