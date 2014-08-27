__author__ = 'shye'
class TrappingRainWater:
    # @param A, a list of Integer
    # @return an integer
    def trap(self, A):
        if A is None:
            return 0
        aLength = len(A)
        if aLength == 1:
            return 0
        leftMaxHeight = [0] * aLength
        rightMaxHeight = [0] * aLength
        maxHeight = 0;
        for i in range(aLength):
            if A[i] > maxHeight:
                maxHeight = A[i]
            leftMaxHeight[i] = maxHeight

        maxHeight = 0
        for i in range(aLength-1, -1, -1):
            if A[i] > maxHeight:
                maxHeight = A[i]
            rightMaxHeight[i] = maxHeight

        total = 0
        for i in range(aLength):
            if min(leftMaxHeight[i], rightMaxHeight[i]) > A[i]:
                total += min(leftMaxHeight[i], rightMaxHeight[i]) - A[i]
        return total
