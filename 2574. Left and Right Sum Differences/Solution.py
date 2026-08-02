class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n
        #compute leftSum
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        #compute rightSum
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]
        #compute answer
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i]) # since it's not saying absolute difference
        return answer
