class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        return sum(1 for w in c1 if c1[w] == 1 and c2[w] == 1)
