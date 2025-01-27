class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for num in nums:
            if nums[:k].count(num) < 2:
                nums[k] = num
                k+=1
        return k