#leetcode Q1004
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        flip = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                flip += 1

            while flip > k:
                if nums[l] == 0:
                    flip -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
