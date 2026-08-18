class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        #count how many subarrays of size k each number appears in
        freq = defaultdict(int)
        
        #for each subarray of size k
        for i in range(n - k + 1):
            #use a set to count each number only once per subarray
            seen = set()
            for j in range(i, i + k):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    freq[nums[j]] += 1
        
        #find the largest number that appears in exactly one subarray
        result = -1
        for num, count in freq.items():
            if count == 1:
                result = max(result, num)
        
        return result
