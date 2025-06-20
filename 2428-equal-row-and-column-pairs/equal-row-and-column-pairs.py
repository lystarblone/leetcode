class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        
        for i in range(len(grid)):
            row = grid[i]
            T = True
            for j in range(len(grid)):
                col = [grid[k][j] for k in range(len(grid))]
                T = True
                if len(row) == len(col):
                    for k in range(len(row)):
                        if row[k] != col[k]:
                            T = False
                            break
                    if T:
                        output += 1
                else:
                    T = False
        
        return output