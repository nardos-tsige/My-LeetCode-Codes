class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_digits = [d for d in str(n) if d != '0']
        x = int(''.join(non_zero_digits)) if non_zero_digits else 0
        digit_sum = sum(int(d) for d in str(x))
        return x * digit_sum
