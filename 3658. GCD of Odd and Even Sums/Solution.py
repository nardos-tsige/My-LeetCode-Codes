class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
# sum of first n odd numbers = n² and 
# sum of the first n even numbers = n(n+1) so
# gcd(n², n(n+1)) = n × gcd(n, n+1) = n × 1 = n
