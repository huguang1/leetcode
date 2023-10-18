"""
739. 每日温度, 每次都将数据按照单调的顺序来排列
"""


def dailyTemperatures(temperatures):
    stack, n = [], len(temperatures)
    ans = [0] * n
    for i, v in enumerate(temperatures):
        while stack and stack[-1][1] < v:
            node = stack.pop()
            ans[node[0]] = i - node[0]
        stack.append((i, v))
    return ans


"""
503. 下一个更大元素 II, 按照单调的的顺序来排列
"""


def nextGreaterElements(nums):
    stack, n = [], len(nums)
    ans = [-1] * n
    for i, v in enumerate(nums + nums):
        while stack and stack[-1][1] < v:
            node = stack.pop()
            if node[0] < n:
                ans[node[0]] = v
        stack.append((i, v))
    return ans


if __name__ == '__main__':
    # temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # ans = dailyTemperatures(temperatures)
    # print(ans)
    nums = [1, 2, 3, 4, 3]
    ans = nextGreaterElements(nums)
    print(ans)



