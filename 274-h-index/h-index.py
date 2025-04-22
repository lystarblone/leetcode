class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        k = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            papers=i+1
            if citations[i]>=papers:
                k = papers
            else:
                break
        return k