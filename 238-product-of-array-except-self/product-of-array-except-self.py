class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_num = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        left = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            right[i]=right[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            left[j]=left[j+1]*nums[j+1]
        for k in range(len(nums)):
            new_num[k] = right[k] * left[k]     
        return new_num