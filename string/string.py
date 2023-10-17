"""
242. 有效的字母异位词， 对数据统计个数
"""
import collections


def anagram(s, t):
    return collections.Counter(s) == collections.Counter(t)


"""
349. 两个数组的交集, 统计数据是否存在
"""


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


"""
202. 快乐数, 统计数据是否存在
"""


def isHappy(n):
    def count(n):
        n = str(n)
        return sum([int(i)**2 for i in n])
    s = set()
    while n != 1:
        s.add(n)
        n = count(n)
        if n in s:
            return False
    return True


"""
1. 两数之和
"""
import collections


def twosum(nums, target):
    d = collections.defaultdict(int)
    for i, v in enumerate(nums):
        if v in d:
            return [d[v], i]
        d[target-v] = i


if __name__ == '__main__':
    # s, t = "anagram", "nagaram"
    # print(anagram(s, t))
    # nums1, nums2 = [1, 2, 2, 1], [2, 2]
    # print(intersection(nums1, nums2))
    # print(isHappy(2))
    nums, target = [2, 7, 11, 15], 9
    print(twosum(nums, target))







