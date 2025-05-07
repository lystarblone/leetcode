class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev_empty = (i==0 or flowerbed[i-1]==0)
                next_empty = (i == len(flowerbed)-1 or flowerbed[i+1]==0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
        
        return n<=0