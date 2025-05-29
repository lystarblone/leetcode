class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        output = []

        for i in range(len(searchWord)):
            current_list = []
            current_prefix = searchWord[:i+1]
            for j in products:
                if j.startswith(current_prefix):
                    current_list.append(j)
                    if len(current_list) == 3:
                        break   
            output.append(current_list)

        return output