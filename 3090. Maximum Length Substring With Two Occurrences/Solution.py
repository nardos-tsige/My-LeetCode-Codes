class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_count = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
