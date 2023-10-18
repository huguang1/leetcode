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
1. 两数之和, 统计数据是否存在
"""
import collections


def twosum(nums, target):
    d = collections.defaultdict(int)
    for i, v in enumerate(nums):
        if v in d:
            return [d[v], i]
        d[target-v] = i


"""
454. 四数相加 II, 对数据统计个数
"""


def fourSum(nums1, nums2, nums3, nums4):
    d = collections.defaultdict(int)
    for i in nums1:
        for j in nums2:
            d[i+j] += 1
    ans = 0
    for i in nums3:
        for j in nums4:
            ans += d.get(-(i+j), 0)
    return ans


"""
383. 赎金信， 对数据统计个数
"""


def canConstruct(ransomNote, magazine):
    d = collections.Counter(magazine)
    d1 = collections.Counter(ransomNote)
    for k, v in d1.items():
        if k not in d or v > d[k]:
            return False
    return True


if __name__ == '__main__':
    # s, t = "anagram", "nagaram"
    # print(anagram(s, t))
    # nums1, nums2 = [1, 2, 2, 1], [2, 2]
    # print(intersection(nums1, nums2))
    # print(isHappy(2))
    # nums, target = [2, 7, 11, 15], 9
    # print(twosum(nums, target))
    # nums1, nums2, nums3, nums4 = [1, 2], [-2, -1], [-1, 2], [0, 2]
    # ans = fourSum(nums1, nums2, nums3, nums4)
    # print(ans)
    ransomNote, magazine = "aa", "ab"
    ans = canConstruct(ransomNote, magazine)
    print(ans)








