__author__ = 'shye'
class JumpGame:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A is None or len(A) == 0:
            return True
        length = len(A)
        maxStep = A[0]
        for i in range(1, length):
            if maxStep >= i:
                maxStep = max(maxStep, A[i]+i)
        if maxStep >= length - 1 :
                return True

        return False