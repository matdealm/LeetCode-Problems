class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    islands += 1

        return islands

    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        lst = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for row, col in lst:
            if row >= 0 and col >=0 and row < len(grid) and col <len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid, row, col) 
