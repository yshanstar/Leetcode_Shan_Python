class MergeSortedArray:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if A is None:
            return B
        if B is None:
            return A

        i = m-1
        j = n-1

        k = m+n-1

        while (i>=0) and (j>=0):
            if B[j] > A[i]:
                A[k] = B[j]
                j-=1
            else:
                A[k] = A[i]
                i-=1
            k-=1

        while j>=0:
            A[k] = B[j]
            j-=1
            k-=1

        return A
