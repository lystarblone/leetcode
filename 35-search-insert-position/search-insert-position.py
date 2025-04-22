class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)-1, -1, -1):
            if target>nums[i]:
                return i+1
        return 0