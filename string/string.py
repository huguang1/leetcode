"""
344. 反转字符串,
"""


def reverseString(s):
    s = s[::-1]
    return s


"""
541. 反转字符串 II
"""


def reverseStr(s, k):
    new = []
    for i in range(0, len(s), k):
        new.append(s[i:i+k])
    ans = ''
    for i, v in enumerate(new):
        if i%2 == 0:
            ans += v[::-1]
        else:
            ans += v
    return ans


"""
151. 反转字符串中的单词
"""


def reverseWords(s):
    s = s.split(' ')
    news = []
    for i in s:
        if i:
            news.append(i)
    return ' '.join(news[::-1])


"""
LCR 122. 路径加密, 字符串替换
"""


def pathEncryption(path):
    return path.replace('.', ' ')


"""
28. 找出字符串中第一个匹配项的下标，匹配字符串
"""


def strStr(haystack, needle):
    l = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i + l] == needle:
            return i
    return -1


"""
459. 重复的子字符串, 匹配字符串
"""


def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if s[:i] * (n // i) == s:
            return True
    return False


if __name__ == '__main__':
    # ans = reverseString('abd')
    # print(ans)
    # s, k = "abcdefg", 2
    # ans = reverseStr(s, k)
    # print(ans)
    # path = "a.aef.qerf.bb"
    # ans = pathEncryption(path)
    # print(ans)
    # haystack, needle = "sadbutsad", "sad"
    # ans = strStr(haystack, needle)
    # print(ans)
    s = "abab"
    ans = repeatedSubstringPattern(s)
    print(ans)




