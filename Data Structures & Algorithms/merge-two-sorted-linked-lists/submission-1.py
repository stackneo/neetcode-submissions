# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = list1
        curr_l2 = list2
        curr = dummy = ListNode(0)
        while curr_l1 and curr_l2:
            print(curr_l1.val, curr_l2.val)
            if curr_l1.val <= curr_l2.val:
                curr.next = ListNode(curr_l1.val)
                curr = curr.next
                curr_l1 = curr_l1.next
            else:
                curr.next = ListNode(curr_l2.val)
                curr = curr.next
                curr_l2 = curr_l2.next
        
        if curr_l1 is not None:
            while curr_l1:
                curr.next = ListNode(curr_l1.val)
                curr = curr.next
                curr_l1 = curr_l1.next
        elif curr_l2 is not None:
            while curr_l2:
                curr.next = ListNode(curr_l2.val)
                curr = curr.next
                curr_l2 = curr_l2.next
        return dummy.next