class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict={}
        for i, num in enumerate(nums):
            if num in nums_dict and (abs(i-nums_dict[num])<=k):
                    return True
            else:
                nums_dict[num]=i
        return False