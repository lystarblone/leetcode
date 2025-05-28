class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        bin_c = bin(c)[2:]

        max_len = max(len(bin_a), len(bin_b), len(bin_c))

        bin_a = bin_a.zfill(max_len)
        bin_b = bin_b.zfill(max_len)
        bin_c = bin_c.zfill(max_len)

        k=0
        
        for i in range(max_len):
            if bin_c[i]=='0':
                if bin_a[i]=='1':
                    k+=1
                if bin_b[i]=='1':
                    k+=1
            else:
                if bin_a[i]=='0' and bin_b[i]=='0':
                    k+=1
        return k