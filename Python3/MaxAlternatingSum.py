class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        squares = []
        for i in range(len(nums)):
            squares.append(nums[i]**2)

        squares.sort(reverse=True)

        total = 0
        low = 0
        high = len(squares)
        if len(squares) % 2 == 0:
            mid = (low + high) // 2
        else:
            mid = (low + high) // 2 + 1
      
        for i in range(mid):
            total += squares[i]

        for i in range(mid, len(squares)):
            total -= squares[i]

        
        return total


if __name__ == "__main__":
    nums = [1, -1, 2, -2, 3, -3]

    sol = Solution()
    print(sol.maxAlternatingSum(nums))