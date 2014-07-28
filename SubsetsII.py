__author__ = 'shye'

class SubsetsII:
    # @Param num, a list of Integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def dfs(depth, start, valueList):
            if valueList not in res:
                res.append(valueList)
            if depth == len(S):
                return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valueList+[S[i]])

        S.sort()
        res = []
        dfs(0, 0, [])
        return res

