# Find First and Last Position of Element in Sorted Array

## Problem Statement
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1:
**Input:** `nums = [5,7,7,8,8,10]`, `target = 8`
**Output:** `[3,4]`

### Example 2:
**Input:** `nums = [5,7,7,8,8,10]`, `target = 6`
**Output:** `[-1,-1]`

### Example 3:
**Input:** `nums = []`, `target = 0`
**Output:** `[-1,-1]`

## Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

## Solution Approach
The solution uses Python's built-in list methods to find the first and last occurrence:

1. **First occurrence:** `nums.index(target)` - finds the leftmost index
2. **Last occurrence:** Finds the rightmost by searching in the reversed list
3. **Edge case:** Returns `[-1, -1]` if target not found

## Time Complexity
- **Time:** O(n) - `index()` and `in` operations scan the list
- **Space:** O(1) - only constant extra space used

## Alternative Approaches
- **Binary Search (O(log n)):** Use two binary searches to find left and right bounds
- **Two Pointers:** Scan from both ends towards the middle
- **Linear Scan:** Simple loop to collect all indices
