class Solution:
    def isUgly(self, n: int) -> bool:
        if (n <= 0):
            return False
            # if 2, 3, 5 are the only prime divisors the number end up being 1 dividing by them each time so it's ugly
        while (n % 2 == 0):
            n /= 2
        while (n % 3 == 0):
            n /= 3
        while (n % 5 == 0):
            n /= 5
        return n == 1
