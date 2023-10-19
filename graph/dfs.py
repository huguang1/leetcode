"""
200. 岛屿数量
"""


def numIslands(grid):
    ans, m, n = 0, len(grid), len(grid[0])

    def dfs(x, y):
        grid[x][y] = '0'
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in direct:
            if 0 <= x+i < m and 0 <= y + j < n and grid[x + i][y + j] == '1':
                dfs(x + i, y + j)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ans += 1
                dfs(i, j)
    return ans


"""
695. 岛屿的最大面积
"""


def maxAreaOfIsland(grid):
    ans, m, n = 0, len(grid), len(grid[0])

    def dfs(x, y):
        num = 1
        grid[x][y] = 0
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in direct:
            if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] == 1:
                num += dfs(x + i, y + j)
        return num
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ans = max(ans, dfs(i, j))
    return ans


"""
1020. 飞地的数量
"""


def numEnclaves(grid):
    m, n, ans = len(grid), len(grid[0]), 0

    def dfs(x, y):
        num = 1
        grid[x][y] = 0
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in direct:
            if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] == 1:
                num += dfs(x + i, y + j)
        return num
    for i in [0, m - 1]:
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
    for i in range(m):
        for j in [0, n - 1]:
            if grid[i][j] == 1:
                dfs(i, j)
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == 1:
                ans += dfs(i, j)
    return ans





