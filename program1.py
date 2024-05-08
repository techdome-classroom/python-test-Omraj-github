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
            
        nrow, ncol = len(grid), len(grid[0])
        visited = [ [false]*ncol for_in range(nrow)]

        island_count = 0
        for i in range(grid[][])
        def count(row, col, count, visited):
                        def getTotalIsles(self, grid:
                 list[list[str]]) -> int:
                     def explore_island(row, col, visited):
                     directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
                     visited[row][col]= True
                     for dr, dc in directions:
                     new_row, new_col= row + dr, col + dc
                     if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "L" and not visited[new_row][new_col]:
                     explore_island(new_row, new_col, visited)

                     if not grid:
                     return 0

                     num_rows, num_cols= len(grid), len(grid[0])
                     visited= [[False] * num_cols for _ in range(num_rows)]

                     island_count= 0
                     for i in range(num_rows):
                     for j in range(num_cols):
                     if grid[i][j] == "L" and not visited[i][j]:
                     explore_island(i, j, visited)
                     island_count += 1

                     return island_count

                     # Test cases
                     solution= Solution()
                     grid1= [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],


]

    grid2 = [
["L", "L", "W", "W", "W"],
["L", "L", "W", "W", "W"],
["W", "W", "L", "W", "W"],
["W", "W", "W", "L", "L"],
]

    print(solution.getTotalIsles(grid1))  # Output: 1
    print(solution.getTotalIsles(grid2))  # Output: 3

        return 0