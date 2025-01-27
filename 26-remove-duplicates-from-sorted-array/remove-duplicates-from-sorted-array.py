class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        i = 0

        for num in nums:
            if num not in nums[:i]:
                nums[k] = nums[i]
                k+=1
            i+=1
        return k