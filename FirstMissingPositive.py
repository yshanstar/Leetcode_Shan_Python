class FirstMissingPositive:
    def firstMissingPositive(self, A):
        length = len(A)
        for i in xrange(length):
            while A[i] != i+1:
                if A[i] <= 0 or A[i] > length or A[i] == A[A[i]-1]:
                    break
                t = A[A[i]-1]
                A[A[i]-1] = A[i]
                A[i] = t

        for i in xrange(length):
            if A[i] != i+1:
                return i+1

        return length+1

