class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {
            'I': 1,
            'V': 5, 
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        summation = 0
        for i in range(len(s)):
            current_value = roman_number[s[i]]
            if i + 1 < len(s) and current_value < roman_number[s[i + 1]]:
                summation -= current_value
            else:
                summation += current_value
    
        return summation
