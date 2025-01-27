class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        origin_x=x
        reversed_x=0
        
        while x>0:
            reversed_x=reversed_x*10+x%10
            x//=10
        return origin_x==reversed_x