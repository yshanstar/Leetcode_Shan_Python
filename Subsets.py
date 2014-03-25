class Subsets:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()

        res = []
        route = []
        self.solve(S, 0, res, route)
        return res

    def solve(self, S, i, res, route):
        if i == len(S):
            res.append([item for item in route])
            return

        self.solve(S, i+1, res, route)
        route.append(S[i])
        self.solve(S, i+1, res, route)
        route.pop()
