class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        '''
        k=0
        for i in range(len(prices)):
            max_num=max(prices[i:])
            if prices[i]>max_num:
                continue
            else:
                k=max(k, (max_num-prices[i]))
        return k
        '''
        k=0
        min_price=100000000
        for i in prices:
            min_price=min(i, min_price)
            k1=i-min_price
            k=max(k, k1)
        return k