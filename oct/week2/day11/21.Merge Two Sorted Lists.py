#leetcode Q21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        minl1 = list1.val
        minl2 = list2.val

        if minl2 < minl1:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        temp = head
        while list1 or list2:
            if not list2:
                head.next = list1
                list1 = list1.next
            elif not list1:
                head.next = list2
                list2 = list2.next
            else:
                val1 = list1.val
                val2 = list2.val
                if (val2 < val1):
                    head.next = list2
                    list2 = list2.next

                else:
                    head.next = list1
                    list1 = list1.next
            head = head.next
        return temp





