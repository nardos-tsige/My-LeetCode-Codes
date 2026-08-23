class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_str = str(n)
        reversed_str = n_str[::-1]
        reversed_n = int(reversed_str)
        return abs(n - reversed_n)
