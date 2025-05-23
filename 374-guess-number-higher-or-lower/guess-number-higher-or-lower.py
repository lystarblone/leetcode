# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left<right:
            middle=left+(right-left)//2
            result = guess(middle)
            if result==0:
                return middle
            elif result==-1:
                right=middle-1
            else:
                left=middle+1
        return left