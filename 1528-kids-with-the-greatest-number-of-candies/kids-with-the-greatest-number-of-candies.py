class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = [False for _ in range(len(candies))]
        max_num = max(candies)

        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_num:
                output[i] = True
        
        return output