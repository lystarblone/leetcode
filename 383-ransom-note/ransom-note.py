class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        words_dict = {}
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i, '', 1)
            else:
                return False
        return True