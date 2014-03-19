class GenerateParentheses:
    def generateParenthesis(self, n):
        GenerateParentheses.n = n
        GenerateParentheses.res = []
        self.gen('', 0, 0)
        return GenerateParentheses.res

    def gen(self, s, leftParenNum, rightParenNum):
        if leftParenNum == rightParenNum == GenerateParentheses.n:
            GenerateParentheses.res.append(s)
            return

        if leftParenNum < GenerateParentheses.n:
            self.gen(s + '(', leftParenNum + 1, rightParenNum)
        if rightParenNum < leftParenNum <= GenerateParentheses.n:
            self.gen(s + ')', leftParenNum, rightParenNum + 1)

        return


