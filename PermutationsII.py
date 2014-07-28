__author__ = 'shye'
class PermutationsII:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        length = len(num)
        if length == 0:
            return
        if length == 1:
            return [num]
        num.sort()
        res = []
        preNum = None
        for cur in range(length):
            if num[cur] == preNum:
                continue
            preNum = num[cur]
            for j in self.permuteUnique(num[0:cur] + num[cur + 1:]):
                res.append([num[cur]] + j)
        return res