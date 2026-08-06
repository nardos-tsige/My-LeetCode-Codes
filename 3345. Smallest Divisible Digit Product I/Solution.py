class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(num):
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        current = n
        while True:
            if digit_product(current) % t == 0:
                return current
            current += 1
