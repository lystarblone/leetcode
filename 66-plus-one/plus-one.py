class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            else:
                if i!=0 and digits[i]!=9:
                    digits[i]+=1
                    return digits
                elif i!=0 and digits[i]==9:
                    digits[i]=0
                else: 
                    if digits[i]==9:
                        digits[i]=0
                        return [1]+digits