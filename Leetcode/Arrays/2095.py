# Delete the Middle Node of a Linked List



from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        x,y=dummy,head
        while y and y.next:
            x=x.next
            y=y.next.next
        x.next=x.next.next
        return dummy.next