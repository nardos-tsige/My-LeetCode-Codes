class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()
        for ch in word:
            if ch.islower():
                lower_set.add(ch)
            else:
                upper_set.add(ch.lower())  
        count = 0
        for ch in lower_set:
            if ch in upper_set:
                count += 1
        
        return count
