    #Definition for singly-linked list.

'''
LeetCode 203
    -head deleted 
    -prev.next = prev.next.next
    
TC: O(N+M)
'''
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums) #O(N)
        fakeH = ListNode(0, head)
        p = fakeH
        #O(M)
        while p.next:
            if p.next.val in numsSet:
                p.next = p.next.next
            else:
                p = p.next
        return fakeH.next