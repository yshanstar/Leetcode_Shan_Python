class ReverseInteger:
    def reverse(self, x):
        flag =0
        if x < 0:
            flag = 1
            x = -x

        result = 0

        while x > 0:
            result = result*10 + x%10
            x /= 10

        if flag > 0:
            result = -result

        return result


mySolution = ReverseInteger()
num = mySolution.reverse(123)
print (num)
num = mySolution.reverse(-123)
print (num)
