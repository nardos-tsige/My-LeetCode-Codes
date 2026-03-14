class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nummy = sorted(set(nums))
        k = len(nummy)
        for i in range(k):
            nums[i] = nummy[i]
        return k
