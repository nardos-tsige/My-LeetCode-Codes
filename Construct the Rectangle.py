class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(area ** 0.5)  #start from square root because that's where L and W are closest
        
        while area % w != 0:   #find the largest w that divides area evenly
            w -= 1
        
        return [area // w, w]
