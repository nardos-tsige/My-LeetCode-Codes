/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    if (nums.length === 0) return [];
    
    const minVal = Math.min(...nums);
    const maxVal = Math.max(...nums);
    const numsSet = new Set(nums);
    
    const missing = [];
    for (let num = minVal; num <= maxVal; num++) {
        if (!numsSet.has(num)) {
            missing.push(num);
        }
    }
    
    return missing;
};
