# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None
        current = second

        while current:
            nxt = current.next

            current.next = previous
            previous = current
            current = nxt           

        
        first = head
        second = previous

        while first and second:
            temporary1 = first.next
            temporary2 = second.next

            first.next = second
            second.next = temporary1

            first = temporary1
            second = temporary2



        
        