"""
206. 反转链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


"""
24. 两两交换链表中的节点
"""


def swap(head):
    cur = dummy = ListNode(0, head)
    while cur and cur.next and cur.next.next:
        cur1 = cur.next
        cur2 = cur.next.next
        cur3 = cur.next.next.next
        cur.next = cur2
        cur2.next = cur1
        cur1.next = cur3
        cur = cur1
    return dummy.next


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    cur = dummy = ListNode()
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    # ans = reverse(dummy.next)
    # while ans:
    #     print(ans.val)
    #     ans = ans.next
    ans = swap(dummy.next)
    while ans:
        print(ans.val)
        ans = ans.next

