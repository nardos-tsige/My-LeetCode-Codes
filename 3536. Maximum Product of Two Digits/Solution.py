class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted((int(d) for d in str(n)), reverse=True)
        return digits[0] * digits[1]
