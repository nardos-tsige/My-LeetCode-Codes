class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original_n = n
        digit_sum = 0
        digit_product = 1
        
        #process digits without converting to string
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10
        
        divisor = digit_sum + digit_product
        return original_n % divisor == 0
