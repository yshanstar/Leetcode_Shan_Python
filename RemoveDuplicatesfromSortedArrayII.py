__author__ = 'shye'
class RemoveDuplicatesfromSortedArrayII:
    #@param A a list of integers
    #@return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 1:
            return length
        duplicate = A[0]
        end = 1
        count = 1
        for i in range(1, length):
            if A[i] == duplicate:
                count += 1
                if count <= 2:
                    A[end] = A[i]
                    end += 1
            else:
                A[end] = A[i]
                end += 1
                duplicate = A[i]
                count = 1
        return end

my_account = RemoveDuplicatesfromSortedArrayII()
print(my_account.removeDuplicates([1,2]))