#leetcode Q27
# used a similar approach to move zeros but move val instead and count
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l=0
        r=0
        count =0
        while r<len(nums):
            while l < len(nums) and nums[l] != val:
                l += 1
                r+=1
                count+=1

            while r < len(nums) and nums[r] == val:
                r += 1
            if l<len(nums) and r<len(nums):
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                count+=1
            else:
                break
        return count