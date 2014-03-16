__author__ = 'sye'
class ThreeSum:
    def threeSum(self, num):
        res = []

        if len(num) < 3:
            return res

        num.sort()
        for i in range(0, len(num)-2 ) :
            if i != 0 and num[i] == num[i-1]:
                continue

            j = i+1
            k = len(num) -1
            while j<k :
                sum = num[i] + num[j] + num[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    tup = [num[i], num[j], num[k]]
                    res.append(tup)
                    k -= 1
                    j += 1

                    while (j<k and num[j] == num[j-1]):
                        j += 1

                    while(j<k and num[k] == num[k+1]):
                        k -= 1

        return res

tSum = ThreeSum()
tSum.threeSum([])
