'''
Method: Two Traversal
Time Complexity: O(L)
Space Complexity: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode()
        node.next = head

        length = 0

        first = ListNode()
        first = head

        while not first.next == None:
            length += 1
            first = first.next

        length = length - n + 1
        first = node
        while length > 0:
            length -= 1
            first = first.next

        if not first.next.next:
            first.next = None
        else:
            first.next = first.next.next
        return node.next

'''
Method2: One Pass Algorithm
Time Complexity: O(L)
Space Complexity: O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode()
        node.next = head

        first = ListNode()
        first = node

        second = ListNode()
        second = node

        for i in range(1, n + 2):
            first = first.next

        while not first == None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return node.next



