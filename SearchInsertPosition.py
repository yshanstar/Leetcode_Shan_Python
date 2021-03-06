class SearchInsertPosition:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1

        while left <= right :
            mid = (right + left)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return mid if target < A[mid] else mid + 1

