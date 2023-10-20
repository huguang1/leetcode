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


"""
122. 买卖股票的最佳时机 II
"""


def maxProfit(prices):
    n = len(prices)
    dp = [0] * n
    for i in range(1, n):
        dp[i] = max(0, prices[i] - prices[i - 1])
    return sum(dp)


"""
45. 跳跃游戏 II
"""


def jump(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i] + 1, dp[i + j])
    return dp[n - 1]


"""
134. 加油站
"""


def canCompleteCircuit(gas, cost):
    n = len(gas)
    dp, ans, left = [1] * n, -1, 0
    for i in range(n * 2):
        i = i % n
        if left + gas[i] >= cost[i]:
            left += gas[i] - cost[i]
            dp[i] = 0
            if ans == -1:
                ans = i
        else:
            dp, ans, left = [1] * n, -1, 0
    if sum(dp) != 0:
        return -1
    return ans








