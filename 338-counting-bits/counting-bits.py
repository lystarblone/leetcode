class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(n+1):
            bin_n = bin(i)
            output.append(str(bin_n).count('1'))
        return output