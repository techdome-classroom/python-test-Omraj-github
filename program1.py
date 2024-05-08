class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        def islandsExp(row, col, visited):
            directions = [(-1,0),(0,1), (1, 0),(0, -1)]
            visited[row][col] = True

            for dr, dc in directions:
                nrow = row+dr, ncol = col+dc
                islandsExp(nrow, ncol, visited)


        return 0