__author__ = 'shye'
class UniquePaths:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[1] for i in range(m)]

        for i in range(n):
            dp[0].append(1)
        for i in range(1, m):
            for j in range(1,n):
                dp[i].append(dp[i-1][j] + dp[i][j-1])
        return dp[m-1][n-1]