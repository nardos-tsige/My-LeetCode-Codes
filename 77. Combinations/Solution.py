class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current):
            if len(current) == k:
                result.append(current[:])
                return
            
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(1, [])
        return result
