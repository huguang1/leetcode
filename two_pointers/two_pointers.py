"""
27. 移除元素, 一个指针，加上一个循环
"""


def removeElement(nums, val):
    slow = 0
    for i in nums:
        if i != val:
            nums[slow] = i
            slow += 1
    return slow


"""
19. 删除链表的倒数第 N 个结点, 快慢指针最容易实现
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    fast = slow = dummy = ListNode(0, head)
    for _ in range(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


"""
15. 三数之和, 多个指针
"""


def threeSum(nums):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i+1, n-1
        while l < r:
            if l > i + 1 and nums[l] == nums[l - 1]:
                l += 1
                continue
            if r < n - 1 and nums[r] == nums[r + 1]:
                r -= 1
                continue
            sums = nums[i]+nums[l]+nums[r]
            if sums == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
            elif sums > 0:
                r -= 1
            else:
                l += 1
    return ans


"""
18. 四数之和, 多个指针
"""


def fourSum(nums, target):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, n - 1
            while l < r:
                if l > j + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < n - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                sums = nums[i] + nums[j] + nums[l] + nums[r]
                if sums == target:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                elif sums > target:
                    r -= 1
                else:
                    l += 1
    return ans


if __name__ == '__main__':
    # nums, val = [3, 2, 2, 3], 3
    # ans = removeElement(nums, val)
    # print(ans)
    # l1 = [4, 1, 8, 4, 5]
    # cur1 = dummy1 = ListNode()
    # for i in l1:
    #     cur1.next = ListNode(i)
    #     cur1 = cur1.next
    # ans = removeNthFromEnd(dummy1.next, 3)
    # while ans:
    #     print(ans.val)
    #     ans = ans.next
    # nums = [-1, 0, 1, 2, -1, -4]
    # ans = threeSum(nums)
    # print(ans)
    nums, target = [1, 0, -1, 0, -2, 2], 0
    ans = fourSum(nums, target)
    print(ans)



