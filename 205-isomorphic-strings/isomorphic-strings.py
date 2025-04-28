class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        words_dict = {}
        for i, j in zip(s, t):
            if i in words_dict:
                if words_dict[i]!=j:
                    return False
            else:
                if j in words_dict.values():
                    return False
                words_dict[i]=j
        return True