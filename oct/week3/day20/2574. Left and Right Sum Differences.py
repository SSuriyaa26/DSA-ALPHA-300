#leetcode 2574
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]
        rightsum=[sum(nums)-nums[0]]
        res=[]
        for i in range(len(nums)):
            leftsum.append(leftsum[i]+nums[i])
        for i in range(1,len(nums)):
            rightsum.append(rightsum[i-1]-nums[i])
        for i in range (len(nums)):
            res.append(abs(leftsum[i]-rightsum[i]))
        return res
