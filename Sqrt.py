class Sqrt:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		left = 0
        right = 46340 # sqrt (C MAX_INT 2147483647)=46340.950001
        
        while left <= right:
            mid = (right + left)/2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                right = mid - 1
            else :
                left = mid + 1
        
        return left