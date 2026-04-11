class Solution:
    def reverseWords(self, s: str) -> str:
        st = ''
        sp = s.split(" ")
        for i in range(len(sp)):
            sp[i] = sp[i][::-1]
            st += sp[i]
            if i < len(sp) - 1:
                st += " "
        return st
