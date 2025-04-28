class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_history=[n]

        if n==1:
            return True
    
        while n!=1:
            s=0
            for i in str(n):
                s+=int(i)**2
            n=s
            if s==10**(len(str(s))-1):
                return True
            else:
                if n in n_history:
                    return False
                n_history.append(n)