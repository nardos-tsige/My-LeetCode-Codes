class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
            
        summation = 1 
        for i in range(2, int(num** 0.5) + 1):
            if num % i == 0:
                summation += i
                if i != num // i:  #avoid adding twice if it's a perfect square
                    summation += num // i
                    
        return summation == num
