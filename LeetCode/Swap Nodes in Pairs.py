# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None: # condition when no nodes in list
            return None
        if head.next == None: # condition when only one node in list
            return head
        if head.next.next == None:
            temp = head.next
            head.next = temp.next
            temp.next = head
            return temp
        else:
            temp = head.next
            head.next = temp.next
            temp.next = head
            head = temp
            head.next.next=self.swapPairs(head.next.next) # linking to the rest of the list
            return head
