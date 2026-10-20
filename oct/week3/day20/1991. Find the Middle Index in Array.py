#leetcode Q1991
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        leftsum = [0]
        rightsum = [sum(nums) - nums[0]]
        for i in range(len(nums)):
            leftsum.append(leftsum[i] + nums[i])
        for i in range(1, len(nums)):
            rightsum.append(rightsum[i - 1] - nums[i])

        for i in range(len(nums)):
            if leftsum[i] == rightsum[i]:
                return i
        return -1
