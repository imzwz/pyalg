class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
def nonrecurse(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    newHead = head
    while cur:
        newHead = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return newHead

def recurse(head):
    if head is None or head.next is None:
        return head
    else:
        newHead = recurse(head.next)
        head.next.next = head
        head.next = None
        return newHead


