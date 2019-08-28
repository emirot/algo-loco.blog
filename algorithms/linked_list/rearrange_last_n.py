# class ListNode():
#   def __init__(self, x):
#     self.value = x
#     self.next = None


def rearrangeLastN(l, n):
    if not l or n == 0:
        return l
    cnt = 0
    tmp = l
    last_pointer = None
    while tmp:
        cnt += 1
        last_pointer = tmp
        tmp = tmp.next

    print("cnt", cnt, n)
    if n == cnt:
        return l
    cut_point = cnt - n

    j = 0
    tmp = l
    link_ptr = None
    while j < cut_point:
        link_ptr = tmp
        print(tmp.value)
        tmp = tmp.next
        j += 1

    prev_head = l
    l = link_ptr.next
    last_pointer.next = prev_head
    link_ptr.next = None

    return l

