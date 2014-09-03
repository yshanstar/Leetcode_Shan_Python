__author__ = 'shye'
class Candy:
    # @param ratings, a list of integers
    # @return an integer
    def candy(self, ratings):
        candies = [1 for i in range(len(ratings))]
        for i in range(len(ratings) - 1):
            if ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                candies[i+1] = candies[i] + 1

        for i in reversed(range(1, len(ratings))):
            if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                candies[i-1] = candies[i] + 1
        return sum(candies)

test = Candy()
print(test.candy([1,0,2]))