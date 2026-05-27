class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #track the last position of each lowercase letter
        last_lower = {}
        #track the first position of each uppercase letter
        first_upper = {}
        #record last occurrence of each lowercase letter
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                #for uppercase, only record the first occurrence
                if ch not in first_upper:
                    first_upper[ch] = i
        count = 0
        #check each potential special character
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch in last_lower and ch.upper() in first_upper:
                #all lowercase must appear before first uppercase
                if last_lower[ch] < first_upper[ch.upper()]:
                    count += 1
        return count
