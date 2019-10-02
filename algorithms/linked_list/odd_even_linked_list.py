# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        i = 0
        tmp = head
        first = True
        prev = None
        tmp_even_head = None
        tail = None
        while tmp:
            if i % 2 != 0:
                if first:
                    second_list = ListNode(tmp.val)
                    tmp_even_head = second_list
                    second_list.next = None
                    first = False
                else:
                    second_list.next = ListNode(tmp.val)
                    second_list = second_list.next
                    second_list.next = None
                if tmp and tmp.next:
                    prev.next = tmp.next
            else:
                tail = tmp
                prev = tmp
            tmp = tmp.next
            i += 1
        if tmp_even_head:
            tail.next = tmp_even_head
        return head
