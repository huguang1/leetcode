"""
707. 设计链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()

    def get(self, index):
        if self.size <= index:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if self.size < index:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        next = cur.next
        cur.next = ListNode(val)
        cur = cur.next
        cur.next = next
        self.size += 1

    def deleteAtIndex(self, index):
        if self.size <= index:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


if __name__ == '__main__':
    obj = LinkList()
    obj.addAtHead(3)
    obj.addAtTail(4)
    obj.addAtIndex(1, 2)
    obj.deleteAtIndex(2)
    param_1 = obj.get(1)
    print(param_1)





