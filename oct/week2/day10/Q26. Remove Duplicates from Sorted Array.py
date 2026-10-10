#leetcode Q26
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]

        return l + 1 #l basically also acts as count as everytime the swap happens is a count of non duplicate val and l increaments

