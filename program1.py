class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
       def explore_island(row, col, vis):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            vis[row][col] = True
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "L" and not visited[new_row][new_col]:
                    explore_island(new_row, new_col, vis)

        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        visited = [[False] * num_cols for _ in range(num_rows)]

        island_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "L" and not visited[i][j]:
                    explore_island(i, j, visited)
                    island_count += 1

        return island_count

                

        return 0