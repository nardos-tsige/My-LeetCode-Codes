class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        coins = 1
        
        while n >= coins:
            n -= coins
            rows += 1
            coins += 1
        return rows
