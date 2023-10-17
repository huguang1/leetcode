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


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    ans = sort(nums)
    print(ans)

