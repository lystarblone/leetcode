class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
                    
        minw=min(strs, key=len)

        for i in range(len(minw)):
            for j in strs:
                if minw[:i+1]!=j[:i+1]:
                    return minw[:(i)]
        return minw