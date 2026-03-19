# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while (left <= right):

            mid_num = (left + right) // 2
            result = guess(mid_num)
            if result == 0:
                return mid_num #we found it
            elif result == -1:
                right = mid_num - 1 #our guess was higher 
            else:
                left = mid_num + 1# our guess was lower
