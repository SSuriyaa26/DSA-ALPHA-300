# leetcode Q350
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_count = {}
        for i in range(len(nums1)):
            nums1_count[nums1[i]] = nums1_count.get(nums1[i],
                                                    0) + 1  # made a counter hashmap (learnt about .get in python , would use getOrDefault in java)

        result = list()  # initialised the result
        for i in range(len(nums2)):
            if nums2[i] in nums1_count:
                if (nums1_count[nums2[i]] <= 0):
                    continue
                    # didnt pass a test case cause repeating values , used this if statement to avoid it
                nums1_count[nums2[i]] -= 1  # decrement counter whenever its found
                result.append(nums2[i])
        return result
