class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output=[]
        current_str = []
        i = 0
        
        while i < len(words):
            line_length = 0 if not current_str else len(' '.join(current_str))
            
            while i<len(words) and line_length+len(words[i])+(1 if current_str else 0)<=maxWidth:
                current_str.append(words[i])
                line_length = len(' '.join(current_str))
                i += 1
            
            if i == len(words):
                str_data = ' '.join(current_str)
                str_data += ' ' * (maxWidth - len(str_data))
                output.append(str_data)
                return output
            elif len(current_str) == 1:
                str_data = current_str[0] + ' ' * (maxWidth - len(current_str[0]))
                output.append(str_data)
            else:
                words_len = sum(len(word) for word in current_str)
                spaces_needed = maxWidth - words_len
                gaps = len(current_str) - 1
                if gaps == 0:
                    str_data = current_str[0] + ' ' * (maxWidth - len(current_str[0]))
                else:
                    spaces_per_gap = spaces_needed // gaps
                    extra_spaces = spaces_needed % gaps
                    str_data = ''
                    for j in range(len(current_str) - 1):
                        str_data += current_str[j] + ' ' * (spaces_per_gap + (1 if j < extra_spaces else 0))
                    str_data += current_str[-1]
                output.append(str_data)
            
            current_str = []
        
        return output