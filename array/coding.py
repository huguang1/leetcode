"""
977. 有序数组的平方, 双指针
"""
import collections


def sort(nums):
    l, r = 0, len(nums)-1
    ans = collections.deque()
    while l <= r:
        if nums[l]**2 <= nums[r]**2:
            ans.appendleft(nums[r]**2)
            r -= 1
        else:
            ans.appendleft(nums[l]**2)
            l += 1
    return ans


"""
209. 长度最小的子数组，双指针和动态规划都可以
"""


def check(target, nums):
    n = len(nums)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + nums[i-1]
    slow, ans = 0, float('inf')
    for i, v in enumerate(dp):
        while v - dp[slow] >= target:
            ans = min(ans, i-slow)
            slow += 1
    return ans if ans != float('inf') else 0


"""
59. 螺旋矩阵 II, 主要是查看写代码的能力
"""


def matrix(n):
    l, r, t, b = 0, n-1, 0, n-1
    dp, num = [[0]*n for _ in range(n)], 1
    while l <= r and t <= b:
        for j in range(l, r):
            dp[t][j], num = num, num+1
        for i in range(t, b+1):
            dp[i][r], num = num, num+1
        if l < r and t < b:
            for j in range(r-1, l, -1):
                dp[b][j], num = num, num+1
            for i in range(b, t, -1):
                dp[i][l], num = num, num+1
        l, r, t, b = l+1, r-1, t+1, b-1
    return dp


if __name__ == '__main__':
    # nums = [-4, -1, 0, 3, 10]
    # ans = sort(nums)
    # print(ans)

    # target, nums = 7, [2, 3, 1, 2, 4, 3]
    # ans = check(target, nums)
    # print(ans)

    ans = matrix(4)
    print(ans)



