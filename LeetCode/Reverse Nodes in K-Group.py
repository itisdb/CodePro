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
        dummy = ListNode(next = head)
        prev  = dummy
        temp = curr = prev2 = head

        while temp and temp.next:
            for i in range(k):
                if temp :
                    temp = temp.next
                else:
                    return dummy.next
        
            curr.next,curr = temp,curr.next
            for i in range(k-1):
                curr.next,prev2,curr = prev2,curr,curr.next
            prev.next = prev2
            prev = head
            prev2 = head = temp
        
        return dummy.next
        