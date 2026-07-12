class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix_sum = [[0] * self.n for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.prefix_sum[i][j] = matrix[i][j] + (self.prefix_sum[i - 1][j] if i - 1 >= 0 else 0) + (self.prefix_sum[i][j - 1] if j - 1 >= 0 else 0) - (self.prefix_sum[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2][col2] - (self.prefix_sum[row1 - 1][col2] if row1 - 1 >= 0 else 0) - (self.prefix_sum[row2][col1 - 1] if col1 - 1 >= 0 else 0) + (self.prefix_sum[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)