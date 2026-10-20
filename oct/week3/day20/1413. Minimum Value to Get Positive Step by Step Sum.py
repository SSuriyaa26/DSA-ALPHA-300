#leetcode 1413
class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        leftsum=[0]
        for i in range(len(nums)):
            leftsum.append(leftsum[i]+nums[i])
        return abs(min(leftsum))+1