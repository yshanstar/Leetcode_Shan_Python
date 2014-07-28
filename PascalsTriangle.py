class PascalsTriangle:
	# @return a list of lists of integers
	def generate(self, numRows):
		solution = []
        if numRows == 0:
            return solution
        actualRow = [1]
        solution.append(actualRow)
        for i in range(1,numRows):
            previousRow = actualRow
            actualRow=[1]
            for j in range(0,i-1):
                actualRow.append(previousRow[j]+previousRow[j+1])
            actualRow.append(1)
            solution.append(actualRow)
        return solution