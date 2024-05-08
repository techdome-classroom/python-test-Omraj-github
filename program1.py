class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        def islandsExp(row, col, visited):
            directions = [(-1,0),(0,1), (1, 0),(0, -1)]
            visited[row][col] = True

            for dr, dc in directions:
                nrow, ncol = row+dr, col+dc
                if  0 <= nrow < len(grid) & 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == 'L' and not visited[nrow][ncol]):
                    islandsExp(nrow, ncol, visited)

        if not grid:
        return 0            
            
        num_row, n_col = len(grid), len(grid[0])
        visited([false][true])
        def count(row, col, count, visited):

        return 0