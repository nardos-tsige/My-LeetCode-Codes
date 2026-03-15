class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      # The algorithm is just combining each elements of the array, and adding one and again appending in to a list and returning
        st = ''
        for i in range(len(digits)):
            st += str(digits[i])
        s = int(st) + 1
        s = str(s)
        arr = []
        for i in range(len(s)):
            arr.append(int(s[i]))
        return arr
