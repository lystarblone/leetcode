class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        vowel_indices = [i for i, char in enumerate(s_list) if char in vowels]
        left, right = 0, len(vowel_indices)-1

        while left<right:
            s_list[vowel_indices[left]], s_list[vowel_indices[right]] = s_list[vowel_indices[right]], s_list[vowel_indices[left]]
            left+=1
            right-=1
        
        return ''.join(s_list)