__author__ = 'shye'

class RotateImage:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for j in range(length/2):
            for i in range(length):
                matrix[i][j], matrix[i][length-1-j] = matrix[i][length-1-j], matrix[i][j]
        return matrix

