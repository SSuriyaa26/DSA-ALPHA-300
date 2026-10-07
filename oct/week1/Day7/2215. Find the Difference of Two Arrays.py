#  leetcode Q 2215
'''
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        #brute force
        result=[[],[]]
        for i in nums1:
            if i not in nums2 and i not in result[0]: #checks if element in other list and duplicates
                result[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in result[1]:
                result[1].append(i)
        return result
'''