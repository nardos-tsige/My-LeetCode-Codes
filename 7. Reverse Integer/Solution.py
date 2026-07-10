class Solution:
    def reverse(self, x: int) -> int:
        rem = 0
        ana = abs(x)
        while ana > 0:
            s = ana % 10
            rem = (rem * 10) + s
            ana = ana // 10
        if rem >= 2147483648:
            return 0
        if x < 0:
            rem *= -1

        return rem
        
