class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_height = 0
        max_hight = current_height
        for i in gain:
            current_height+=i
            max_hight=max(max_hight, current_height)
        return max_hight