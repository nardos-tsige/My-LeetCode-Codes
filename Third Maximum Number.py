class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #remove duplicates using set
        distinct = list(set(nums))
        #sort tehm in descending order
        distinct.sort(reverse=True)
        #if the total number of elements are less than 3 distinct numbers, return the maximum
        if len(distinct) < 3:
            return distinct[0]
        #otherwise, return the third maximum
        return distinct[2]
