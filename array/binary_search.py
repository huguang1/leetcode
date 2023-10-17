"""
704: 二分查找
其核心逻辑是为了找中点，其难点是边界条件的确立
"""


def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == '__main__':
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    nums1, target1 = [-1, 0, 3, 5, 9, 12],  2
    ans = search(nums1, target1)
    print(ans)


