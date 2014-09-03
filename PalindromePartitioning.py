class PalindromePartitioning:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.s, self.res, self.lenS = s, [], len(s)
        self.isPal = [[False for j in range(self.lenS)] for i in range(self.lenS)]
        for j in range(self.lenS):
            for i in reversed(range(j + 1)):
                if s[i] == s[j] and ( j - i <= 1 or self.isPal[i + 1][j - 1] == True):
                    self.isPal[i][j] = True  # True means substring from s[i](included) to s[j](included) is palindrome
        self.dfs(0, [])
        return self.res

    def dfs(self, start, L):
        if start == self.lenS:
            self.res.append(L)
            return
        for end in range(start, self.lenS):
            if self.isPal[start][end] == True:
                self.dfs(end + 1, L[:] + [self.s[start: end + 1]])  # make a copy of list L and add a substring


