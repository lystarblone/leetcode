class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        roman_nums={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        
        for i in range(len(s)):
            if roman_nums[s[i]]>roman_nums[s[i-1]] and i != 0:
                total+=roman_nums[s[i]]-roman_nums[s[i-1]]*2
            else: 
                total+=roman_nums[s[i]]
        return total