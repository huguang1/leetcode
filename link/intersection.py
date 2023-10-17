"""
面试题 02.07. 链表相交
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def intersection(headA, headB):
    A, B = headA, headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA
    return A


def detectCycle(head):
    fast, slow = head, head
    while True:
        if not (fast and fast.next):
            return
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


if __name__ == '__main__':
    l1 = [4, 1, 8, 4, 5]
    l2 = [5, 0, 1, 8, 4, 5]
    cur1 = dummy1 = ListNode()
    for i in l1:
        cur1.next = ListNode(i)
        cur1 = cur1.next
    cur2 = dummy2 = ListNode()
    for i in l2:
        cur2.next = ListNode(i)
        cur2 = cur2.next
    ans = intersection(dummy1.next, dummy2.next)
    print(ans)



