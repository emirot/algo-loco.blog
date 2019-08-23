# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        ll_size = 0
        tmp = head
    
        while tmp:
            ll_size +=1
            tmp = tmp.next
        stop = ll_size - n
        if ll_size==1 and n == 1:
            return None
        if stop == 0:
            return head.next
        tmp = head
        j = 0
        while j < stop -1:
            tmp = tmp.next
            j +=1
        tmp.next = tmp.next.next
        return head