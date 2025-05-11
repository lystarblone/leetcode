class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        num1_set = set(nums1)
        num2_set = set(nums2)
        return [[x for x in num1_set if x not in num2_set], [x for x in num2_set if x not in num1_set]]