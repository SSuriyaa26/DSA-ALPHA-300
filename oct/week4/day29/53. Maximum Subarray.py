#leetcode Q29
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if currentSum + nums[i] < nums[i]:
                currentSum = nums[i]
            else:
                currentSum += nums[i]

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum