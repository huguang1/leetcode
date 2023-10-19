"""
77. 组合
"""


def combine(n, k):
    l = [i + 1 for i in range(n)]
    ans = []

    def dfs(l, path):
        if len(path) == k:
            ans.append(path)
        for i in range(len(l)):
            dfs(l[i + 1:], path + [l[i]])
    dfs(l, [])
    return ans


"""
216. 组合总和 III
"""


def combinationSum3(k, n):
    l, ans = [i + 1 for i in range(9)], []

    def dfs(l, n, path):
        if len(path) >= k or n <= 0:
            if len(path) == k and n == 0:
                ans.append(path)
            return
        for i in range(len(l)):
            dfs(l[i + 1:], n - l[i], path + [l[i]])
    dfs(l, n, [])
    return ans


"""
17. 电话号码的字母组合
"""


def letterCombinations(digits):
    if not digits:
        return []
    d = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    ans, n = [], len(digits)

    def dfs(digits, path):
        if not digits and len(path) == n:
            ans.append(path)
        for i in range(len(digits)):
            for j in d[digits[i]]:
                dfs(digits[i + 1:], path + j)
    dfs(digits, '')
    return ans


"""
40. 组合总和 II
"""


def combinationSum2(candidates, target):
    candidates.sort()
    ans = []

    def dfs(can, target, path):
        if target <= 0:
            if target == 0:
                ans.append(path)
            return
        for i, v in enumerate(can):
            if i > 0 and can[i] == can[i - 1]:
                continue
            dfs(can[i + 1:], target - can[i], path + [can[i]])
    dfs(candidates, target, [])
    return ans


"""
131. 分割回文串
"""


def partition(s):
    ans = []

    def dfs(s, path):
        if not s:
            ans.append(path)
        for i, v in enumerate(s):
            if s[:i + 1] == s[:i + 1][::-1]:
                dfs(s[i + 1:], path + [s[:i + 1]])
    dfs(s, [])
    return ans


"""
93. 复原 IP 地址
"""


def restoreIpAddresses(s):
    ans = []

    def dfs(s, path):
        if not s or len(path) >= 4:
            if not s and len(path) == 4:
                ans.append(path)
            return
        for i in range(min(3, len(s))):
            if str(int(s[:i + 1])) == s[:i + 1] and int(s[:i + 1]) <= 255:
                dfs(s[i + 1:], path + [s[:i + 1]])
    dfs(s, [])
    return ['.'.join(i) for i in ans]


"""
90. 子集 II
"""


def subsetsWithDup(nums):
    nums.sort()
    ans = []

    def dfs(nums, path):
        ans.append(path)
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            dfs(nums[i + 1:], path + [v])
    dfs(nums, [])
    return ans


"""
491. 递增子序列
"""


def findSubsequences(nums):
    ans = []

    def dfs(nums, path):
        if len(path) >= 2:
            ans.append(path)
        s = set()
        for i, v in enumerate(nums):
            if v not in s and (not path or path[-1] <= v):
                dfs(nums[i + 1:], path + [v])
                s.add(v)
    dfs(nums, [])
    return ans


"""
47. 全排列 II
"""


def permuteUnique(nums):
    nums.sort()
    ans = []

    def dfs(nums, path):
        if not nums:
            ans.append(path)
        for i, v in enumerate(nums):
            if i > 0 and nums[i - 1] == v:
                continue
            dfs(nums[:i] + nums[i + 1:], path + [v])
    dfs(nums, [])
    return ans




