__author__ = 'shye'
class PascalsTriangleII:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex+1):
            curNum = 1
            for j in range(1, i):
                tmp = curNum
                curNum = res[j]
                res[j] = tmp + res[j]
            res.append(1)
        return res