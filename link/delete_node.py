"""
203. 移除链表元素
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(head, val):
    cur = dummy = ListNode(0, head)
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


"""
19. 删除链表的倒数第 N 个结点
"""


def reverse(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def remove_node(head, n):
    cur = dummy = ListNode(0, reverse(head))
    for _ in range(n-1):
        cur = cur.next
    cur.next = cur.next.next
    return reverse(dummy.next)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    cur = dummy = ListNode()
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    # ans = delete_node(dummy.next, 5)
    # while ans:
    #     print(ans.val)
    #     ans = ans.next
    ans = remove_node(dummy.next, 5)
    while ans:
        print(ans.val)
        ans = ans.next



