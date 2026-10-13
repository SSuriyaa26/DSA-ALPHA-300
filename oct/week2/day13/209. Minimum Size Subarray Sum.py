#leetcode Q209
#brute for solution , TLE
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum1=0
        count=0
        min1=float('inf')
        for i in range(len(nums)):
            sum1+=nums[i]
            if nums[i]>=target:
                return 1
            count=1
            for j in range(i+1,len(nums)):
                sum1+=nums[j]
                count+=1
                if sum1>=target:
                    if count<min1:
                        min1=count
                    break
            sum1=0
        return 0 if min1==float(inf) else min1

