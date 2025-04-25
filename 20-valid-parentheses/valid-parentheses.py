class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {')': '(', '}': '{', ']': '['}
        b = []
        for x in s:
            if x in a.values():
                b.append(x)
            elif x in a:
                if not b or b.pop() != a[x]:
                    return False
            else:
                return False
        return True if len(b) == 0 else False