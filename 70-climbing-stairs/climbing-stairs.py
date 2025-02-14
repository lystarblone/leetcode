class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        steps=[0 for _ in range(n)]
        steps[0],steps[1] = 1,2
        for i in range(2, n):
            steps[i]=steps[i-1]+steps[i-2]
        return steps[n-1]