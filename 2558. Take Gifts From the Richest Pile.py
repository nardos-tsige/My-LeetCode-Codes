class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for j in range(k):
            #find the index of the maximum value
            max_idx = 0
            for i in range(len(gifts)):
                if gifts[i] > gifts[max_idx]:
                    max_idx = i
            
            #replace it with its square root--rounded down
            gifts[max_idx] = int(math.sqrt(gifts[max_idx]))
        
        # return the sum
        return sum(gifts)
