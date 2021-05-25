## APPROACH : LINKED LISTS ##
## LOGIC : GREEDY ##

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


#Approach: stack
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.ptr = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.ptr+1] + [url]
        self.ptr = len(self.stack) - 1

    def back(self, steps: int) -> str:
        self.ptr = max(0, self.ptr - steps)
        return self.stack[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr = min(len(self.stack) - 1, self.ptr + steps)
        return self.stack[self.ptr]