class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ''
        for i in range(min(len(word1), len(word2))):
            output = output + word1[i] + word2[i]
        
        if len(word1)>len(word2):
            return output+word1[len(word2):]
        elif len(word1)<len(word2):
            return output+word2[len(word1):]

        return output