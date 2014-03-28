class Triangle:
    def minimumTotal(self, triangle):
        if not triangle:
            return res

        length = len(triangle)

        if length == 1:
            return triangle[0][0]

        dp = [0 for i in xrange(length)]

        for row in xrange(length-1, -1, -1):
            for col in xrange(0, len(triangle[row])):
                if row == length - 1:
                    dp[col] = triangle[row][col]
                    continue
                dp[col] = min(dp[col], dp[col+1]) + triangle[row][col]

        return dp[0]

test = Triangle()
a = [[-10]]
print(test.minimumTotal(a))
