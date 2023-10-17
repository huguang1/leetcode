"""
27: 原地删除某个值，其是用双指针来进行操作
"""


def remove(nums, val):
    slow = 0
    for i in nums:
        if val != i:
            nums[slow] = i
            slow += 1
    return nums


if __name__ == '__main__':
    nums, val = [3, 2, 2, 3, 4, 5], 3
    ans = remove(nums, val)
    print(ans)

