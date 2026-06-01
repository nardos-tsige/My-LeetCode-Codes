class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        freq = [0] * 101
        for c in cost:
            freq[c] += 1
        
        total = 0
        count = 0  #how many candies processed in current group of 3
        #iterate from expensive to cheap
        for price in range(100, 0, -1):
            while freq[price] > 0:
                count += 1
                #pay for 1st and 2nd in group of 3 & skip 3rd
                if count % 3 != 0:
                    total += price
                freq[price] -= 1
        
        return total
