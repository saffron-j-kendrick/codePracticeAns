class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum < 0:
            return ""

        result = []

        for i in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit

        return "".join(result)

if __name__ == "__main__":
    num = 2
    sum = 17
    sol = Solution()
    print(sol.maxSumOfSquares(num, sum))

        
