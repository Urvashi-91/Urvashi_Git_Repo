# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         output = ListNode(0)
#         head = output
#
#         while l1 or l2:
#             v1 = l1.val if l1 else math.inf
#             v2 = l2.val if l2 else math.inf
#             if v1 <= v2:
#                 head.next = l1
#                 l1 = l1.next if l1 else None
#             else:
#                 head.next = l2
#                 l2 = l2.next if l2 else None
#             head = head.next
#
#         return output.next


'''
2nd Approach
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        tail = result

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return result.next

l1 = ListNode().__init__([1,2,3])
Solution().mergeTwoLists([1,2,3],[4,5,6])


