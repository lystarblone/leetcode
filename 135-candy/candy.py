class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        k = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                k[i]=k[i-1]+1
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j]>ratings[j+1] and k[j]<=k[j+1]:
                k[j]=k[j+1]+1
        return sum(k)