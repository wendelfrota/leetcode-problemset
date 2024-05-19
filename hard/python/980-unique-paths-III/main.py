class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start_x = start_y = end_x = end_y = empty_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 2:
                    end_x, end_y = i, j

                if grid[i][j] != -1:
                    empty_count += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y, count):
            if x == end_x and y == end_y:
                return 1 if count == empty_count else 0

            temp = grid[x][y]
            grid[x][y] = -1
            paths = 0

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    paths += dfs(nx, ny, count + 1)

            grid[x][y] = temp
            return paths

        return dfs(start_x, start_y, 1)


# print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
# print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
# print(Solution().uniquePathsIII([[0, 1], [2, 0]]))
