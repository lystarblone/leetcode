class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i, j]
        return False
        """

        words_dict={}
        for i, num in enumerate(nums):
            targ=target-num
            if targ in words_dict:
                return [i, words_dict[targ]]
            words_dict[num]=i
        return False