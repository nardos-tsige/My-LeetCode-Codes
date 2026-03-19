class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (num ** 0.5).is_integer()
