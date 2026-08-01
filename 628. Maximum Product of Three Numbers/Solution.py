class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = float('-inf')
    
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    product = nums[i] * nums[j] * nums[k]
                    max_product = max(max_product, product)
    
        return max_product
