/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    nums1.push(...nums2)
    nums1.sort((a, b) => a - b)
    let n = nums1.length
    if (n % 2 !== 0){
        return nums1[Math.floor(n/2)];
    }
    else {
        return ((nums1[n/2 - 1]) + nums1[n/2])/2
    }
};
