class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        W1, W2 = "", ""
        for i in word1:
            W1 += i
        for j in word2:
            W2 += j
        if W1 == W2:
            return True
        return False
