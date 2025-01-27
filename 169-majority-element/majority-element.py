class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unical_nums = set(nums)
        k = 0
        for num in unical_nums:
            if nums.count(num) > nums.count(k):
                k = num
        return k