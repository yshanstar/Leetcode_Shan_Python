__author__ = 'shye'
class RemoveElement:
    # @param A a list of integers
    # @param elem an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        if length <= 0:
            return length

        end = 0
        for i in A:
            if i != elem:
                A[end] = i
                end += 1
        return end

myTest = RemoveElement()
print (myTest.removeElement([1,2,3,4], 1))