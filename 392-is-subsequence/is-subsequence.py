class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k=0
        if s and t:
            for char in t:
                if char == s[k]:
                    k+=1
                if k==(len(s)) or (k==0 and char==s[k]):
                    return True
        elif not s:
            return True
        return False