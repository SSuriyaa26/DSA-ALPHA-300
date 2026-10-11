#leetcode Q 1313
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0,len(nums)-1,2):
            result+=([nums[i+1]] * nums[i]) #using the logic that arr[0]*5 prints 00000
        return result