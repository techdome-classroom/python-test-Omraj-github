class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        def islandsExp(row, col, visited):
            directions = [(-1,0),(0,1), (1, 0),(0, -1)]
            visited[row][col] = True

            for dr, dc in directions:
                nrow , ncol = col+dc
                if  0<=nrow<=len(grid) & 0 <= ncol < len(grid[0])
                islandsExp(nrow, ncol, visited)


        return 0