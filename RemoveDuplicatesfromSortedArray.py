__author__ = 'shye'
class RemoveDuplicatesfromSortedArray:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A) == 0:
            return 0
        j = 1;
        duplicate = A[0]
        for i in range(1, len(A)):
            if A[i] != duplicate:
                A[j] = A[i]
                j += 1
            duplicate = A[i]
        return j

my_account = RemoveDuplicatesfromSortedArray()
print(my_account.removeDuplicates([1]))
