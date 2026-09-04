class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}
        
        for i in range(len(s)):
            if s[i] in map_s:
                if map_s[s[i]] != t[i]:
                    return False
            else:
                map_s[s[i]] = t[i]
            
            if t[i] in map_t:
                if map_t[t[i]] != s[i]:
                    return False
            else:
                map_t[t[i]] = s[i]
        
        return True
