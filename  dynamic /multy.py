"""
62. 不同路径
"""


def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else 0) + (dp[i][j - 1] if j - 1 >= 0 else 0)
    return dp[m - 1][n - 1]


"""
63. 不同路径 II
"""


def uniquePathsWithObstacles(obstacleGrid):
    o = obstacleGrid
    m, n = len(o), len(o[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if o[0][0] == 0 else 0
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue
            if o[i][j] != 1:
                dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else 0) + (dp[i][j - 1] if j - 1 >= 0 else 0)
    return dp[m - 1][n - 1]


"""
337. 打家劫舍 III
"""


def rob(root):
    def dfs(root):
        if not root:
            return 0, 0
        lno, lrob = dfs(root.left)
        rno, rrob = dfs(root.right)
        return max(lno, lrob) + max(rno, rrob), root.val + lno + rno
    return max(dfs(root))



