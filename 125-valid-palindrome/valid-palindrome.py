class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=''.join(x for x in s if x.isalnum()).lower()
        return s1==s1[::-1]