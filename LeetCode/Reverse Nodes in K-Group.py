# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 1:
            return head
        current = head
        count = 0
        next=None
        prev=None
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next:
            head.next=self.reverseKGroup(next,k)
        return prev       
            