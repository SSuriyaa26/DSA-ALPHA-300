#leetcode Q283
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        l=0
        r=0
        while r<len(nums):
            while l < len(nums) and nums[l] != 0:
                l += 1
                r+=1

            while r < len(nums) and nums[r] == 0:
                r += 1
            if l<len(nums) and r<len(nums):
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            else:
                break
