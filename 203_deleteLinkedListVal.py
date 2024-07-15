from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head, val: int) -> Optional[ListNode]:
        p = fakeH = ListNode(next=head)
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return fakeH.next