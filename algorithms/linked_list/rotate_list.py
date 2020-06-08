class Solution:
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if head and head.next is None:
            return head
        l = 0
        t = head
        while t:
            l +=1
            t = t.next
        while k % l > 0:
            tmp = head
            while tmp.next:
                prev = tmp
                tmp = tmp.next
            tail = tmp
            # remove node. replace tail move to head
            prev.next = None
            tail.next = head
            head = tail
            tail = prev
            k -= 1
        return head
