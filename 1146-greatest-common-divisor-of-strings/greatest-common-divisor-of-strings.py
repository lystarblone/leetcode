class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def can_divide(s, x):
            if len(s) % len(x) != 0:
                return False
            repeat_count = len(s) // len(x)
            return x * repeat_count == s

        for i in range(min(len(str1), len(str2)), 0, -1):
            word = str1[:i]
            if can_divide(str1, word) and can_divide(str2, word):
                return word

        return ''