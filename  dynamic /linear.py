"""
509. 斐波那契数
"""


def fib(n):
    dp = [0] * (n + 1)
    if n == 0:
        return 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


"""
70. 爬楼梯
"""


def climbStairs(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


"""
746. 使用最小花费爬楼梯
"""


def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]


"""
343. 整数拆分
"""


def integerBreak(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]


"""
96. 不同的二叉搜索树
"""


def numTrees(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]


"""
518. 零钱兑换 II
"""


def change(amount, coins):
    dp = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


"""
377. 组合总和 Ⅳ
"""


def combinationSum4(nums, target):
    dp = [1] + [0] * target
    for i in range(1, target + 1):
        for j in nums:
            dp[i] += dp[i - j] if i - j >= 0 else 0
    return dp[target]


"""
322. 零钱兑换
"""


def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1 if i >= coin else float('inf'))
    return dp[amount] if dp[amount] != float('inf') else -1


"""
279. 完全平方数
"""


def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, int(i ** (0.5)) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[-1]


"""
139. 单词拆分
"""


def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[n]


"""
198. 打家劫舍
"""


def rob(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    if n == 1:
        return dp[0]
    dp[1] = max(nums[:2])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return max(dp)


"""
213. 打家劫舍 II
"""


def rob2(nums):
    def check(nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n == 1:
            return dp[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp)
    if len(nums) == 1:
        return nums[0]
    return max(check(nums[1:]), check(nums[:-1]))


"""
337. 打家劫舍 III
"""


"""
121. 买卖股票的最佳时机
"""


def maxProfit(prices):
    n = len(prices)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = max(0, prices[i] - prices[i - 1] + dp[i - 1])
    return max(dp)


"""
122. 买卖股票的最佳时机 II
"""


def maxProfit2(prices):
    n = len(prices)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = max(0, prices[i] - prices[i - 1])
    return sum(dp)


"""
300. 最长递增子序列
"""


def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


"""
674. 最长连续递增序列
"""


def findLengthOfLCIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


"""
53. 最大子数组和
"""


def maxSubArray(nums):
    n = len(nums)
    dp = [float('-inf')] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i]
        if dp[i - 1] > 0:
            dp[i] = dp[i - 1] + nums[i]
    return max(dp)




