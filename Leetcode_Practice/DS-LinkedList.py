class Node:
    def __init__(self, data: None, next: None):
        self.data = data
        self.next = next
class SLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def traverse(self):
        if self.head == None:
            return
        itr = self.head
        value = ""
        while itr:
            value += str(itr.data) + '--->'
            itr = itr.next
        print(value)

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        if self.head == None:
            return 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while index-1 != count:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1







if __name__ == '__main__':
    ll = SLinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_begining(5)
    ll.insert_at_end(6)
    ll.insert_at_end(5)
    ll.insert_list(["1","2","3"])
    ll.remove_at(2)
    ll.insert_at(6,1)
    ll.traverse()