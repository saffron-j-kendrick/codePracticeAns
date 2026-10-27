class Solution:
    def Candy(self, ratings: list[int]) -> int:
        numChildren = len(ratings)
        candyStart = [1] * numChildren
        # left to right
        for i in range(1, numChildren):
            if ratings[i - 1] < ratings[i] and candyStart[i-1] >= candyStart[i]:
                candyStart[i] = candyStart[i - 1] + 1
        # right to left
        for i in range(numChildren - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candyStart[i + 1] >= candyStart[i]:
                candyStart[i] = candyStart[i + 1] + 1

        return sum(candyStart)