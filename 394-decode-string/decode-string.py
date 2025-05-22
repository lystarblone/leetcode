class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_string = ''
        curr_number = 0
        
        for char in s:
            if char.isdigit():
                curr_number = curr_number*10+int(char)
            elif char=='[':
                stack.append((curr_string, curr_number))
                curr_string = ''
                curr_number = 0
            elif char==']':
                prev_string, num = stack.pop()
                curr_string = prev_string+num*curr_string
            else:
                curr_string+=char
        
        return curr_string