#leetcode Q707
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next

        if curr is None:
            return -1

        return curr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = Node(val)

        if self.head is None:
            self.head = new
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head

        for i in range(index - 1):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return

        new = Node(val)
        new.next = curr.next
        curr.next = new

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
            return

        curr = self.head

        for i in range(index - 1):
            if curr is None:
                return
            curr = curr.next

        if curr is None or curr.next is None:
            return

        curr.next = curr.next.next
