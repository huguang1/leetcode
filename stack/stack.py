"""
20. 有效的括号, 其可以暂时存储数据
"""


def isValid(s):
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        else:
            if not stack or i != d[stack.pop()]:
                return False
    return stack == []


"""
1047. 删除字符串中的所有相邻重复项, 可以暂时存储数据
"""


def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


"""
150. 逆波兰表达式求值, 这个也是将数据暂时存储起         
"""


def evalRPN(tokens):
    d = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: int(x/y)
    }
    stack = []
    for i in tokens:
        if i not in d:
            stack.append(i)
        else:
            y, x = stack.pop(), stack.pop()
            stack.append(d[i](int(x), int(y)))
    return int(stack[0])


"""
239. 滑动窗口最大值，用来存储需要的数据
"""
import collections


def maxSlidingWindow(nums, k):
    queue, ans = collections.deque(), []
    for i, v in enumerate(nums):
        if queue and i - queue[0][0] >= k:
            queue.popleft()
        while queue and queue[-1][1] <= v:
            queue.pop()
        queue.append((i, v))
        if i >= k - 1:
            ans.append(queue[0][1])
    return ans


"""
347. 前 K 个高频元素,使用堆进行排序，效率非常高
"""
import heapq


def topKFrequent(nums, k):
    c = collections.Counter(nums)
    heap = []
    for i, v in c.items():
        heapq.heappush(heap, (-v, i))
    ans = []
    for _ in range(k):
        ans.append(heapq.heappop(heap)[1])
    return ans


if __name__ == '__main__':
    # nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    # ans = maxSlidingWindow(nums, k)
    # print(ans)
    nums, k = [1, 1, 1, 2, 2, 3], 2
    ans = topKFrequent(nums, k)
    print(ans)


