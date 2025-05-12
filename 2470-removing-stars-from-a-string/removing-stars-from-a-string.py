class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=[]
        for i in s:
            if i=='*':
                output.pop()
            else:
                output.append(i)
        return ''.join(output)