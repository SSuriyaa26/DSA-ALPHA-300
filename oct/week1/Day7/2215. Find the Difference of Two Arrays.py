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
#optimised solution using sets, removes the check for duplicates
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = [[],[]]
        for i in set1:
            if i not in set2:
                result[0].append(i)

        for i in set2:
            if i not in set1:
                result[1].append(i)
        return result
        
