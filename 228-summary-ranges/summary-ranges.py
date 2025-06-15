class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        output = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = nums[i]
        
        end = nums[-1]
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        
        return output