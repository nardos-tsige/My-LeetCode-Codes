class Solution:
    def isPalindrome(self, s: str) -> bool:

        #the algo - leaving special characters(lowering characters) and checking if the reverse is equal to the original extracted one
        new_s = ""
        for j in s:
            if not (j.isalpha() or j.isalnum()):
                continue
            else:
                new_s += j.lower()
        if new_s == new_s[::-1]:
            return True
        return False
