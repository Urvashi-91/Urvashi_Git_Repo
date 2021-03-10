# Definition for singly-linked list.
'''
Edge Cases:
1. L1 and L2 are of different Sizes
2. L1 and L2 are finished But there is a Carry
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def __init__(self):
        self.head = ListNode()
        #self.l2 = ListNode()

    def insert_at_end(self, val):
        if self.head == None:
            self.head = ListNode(val, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = ListNode(val, None)

    def traverse(self):
        if self.head == None:
            return
        itr = self.head
        value = ""
        while itr:
            value += str(itr.val) + '--->'
            itr = itr.next
        print(value)

    def insert_list(self, data_list):
        self.head = None
        for val in data_list:
            self.insert_at_end(val)

    def addTwoNumbers(self, l1, l2):

        result = ListNode()
        curr_pos = result

        carry = 0
        print(l1, l2, carry)
        while l1 or l2 or carry:

            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            val_res = val_l1 + val_l2 + carry
            carry = val_res // 10
            val_res = val_res % 10

            curr_pos.next = ListNode(val_res)
            # update pointers
            curr_pos = curr_pos.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next



'''
Testing
'''




if __name__ == '__main__':
    sol1 = Solution()
    sol2 = Solution()
    sol3 = Solution()
    l1 = sol1.insert_list([2,3,4])
    l2 = sol2.insert_list([1,2,1])
    sol3.addTwoNumbers(l1,l2)
    #sol1.traverse()
    #sol.traverse()
