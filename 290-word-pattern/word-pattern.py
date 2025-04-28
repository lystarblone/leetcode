class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words_dict = {}
        words = s.split()

        if len(pattern)!=len(words):
            return False
        
        for i, j in zip(pattern, words):
            if i in words_dict:
                if words_dict[i] != j:
                    return False
            else:
                if j in words_dict.values():
                    return False
                words_dict[i] = j
        return True