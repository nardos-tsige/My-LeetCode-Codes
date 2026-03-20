class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        # after merging ... sorting ... then if it's the length of the final merged list is odd return simply the middle element and if it's even we are gonna sum the 2 middle and divide it in to 2
        n = len(nums1)
        if (n % 2 != 0):
            return nums1[int(n/2)]
        else:
            return (nums1[int(n/2) - 1] + nums1[int(n/2)]) / 2
