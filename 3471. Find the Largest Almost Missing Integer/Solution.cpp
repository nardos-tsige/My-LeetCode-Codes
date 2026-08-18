class Solution {
public:
    int largestInteger(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::unordered_map<int, int> freq;
        
        //count how many subarrays of size k each number appears in
        for (int i = 0; i <= n - k; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < i + k; j++) {
                if (seen.find(nums[j]) == seen.end()) {
                    seen.insert(nums[j]);
                    freq[nums[j]]++;
                }
            }
        }
        
        //find the largest number that appears in exactly one subarray
        int result = -1;
        for (auto& [num, count] : freq) {
            if (count == 1) {
                result = std::max(result, num);
            }
        }
        
        return result;
    }
};
