'''
TC: O(N)
SC: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        parts = length // k

        if k <= 1 or head is None:
            return head

        current, previous = head, None
        while True:
            last_node_of_previous_part = previous
            # after reversing the LinkedList 'current' will become the last node of the sub-list
            last_node_of_sub_list = current
            next = None  # will be used to temporarily store the next node
            i = 0
            while current is not None and i < k:  # reverse 'k' nodes
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1
            parts -= 1
            # connect with the previous part
            if last_node_of_previous_part is not None:
                last_node_of_previous_part.next = previous
            else:
                head = previous

            # connect with the next part
            last_node_of_sub_list.next = current

            if current is None or parts <= 0:
                break
            previous = last_node_of_sub_list
        return head


