class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(remain, start, curr_comb):
            if remain == 0:
                output.append(curr_comb[:])
                return
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                curr_comb.append(candidates[i])
                backtrack(remain - candidates[i], i, curr_comb)
                curr_comb.pop()

        output = []
        candidates = sorted(candidates)
        backtrack(target, 0, [])
        return output