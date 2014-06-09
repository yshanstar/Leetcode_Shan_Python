__author__ = 'yshan_000'


class EditDistance:
    # @ return an integer
    def minDistance(self, word1, word2):
        row = len(word1)
        col = len(word2)

        dp = [[0 for j in range(col + 1)] for i in range(row + 1)]

        for i in range(row + 1):
            dp[i][0] = i

        for j in range(col + 1):
            dp[0][j] = j

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[row][col]

s = EditDistance();
s.minDistance("a", "ab")