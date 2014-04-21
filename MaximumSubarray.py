class MaximumSubarray:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) is 0:
            return 0

        res  = A[0]
        tmp = 0

        for x in A:
            tmp = tmp + x
            res =  max(res, tmp)
            if tmp < 0:
                tmp = 0

        return res

