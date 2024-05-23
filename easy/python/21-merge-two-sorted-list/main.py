from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def mergeTwoLists(self, list1, list2):
        head = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return head.next