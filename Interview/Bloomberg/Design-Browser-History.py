class BrowserHistory():
    def __init__(self):
        self.stack_list = []

    def visited(self, url):
        if url in self.stack_list:
            self.stack_list.remove(url)
        self.stack_list.append(url)

    def showHistory(self):
        if not self.stack_list:
            return None
        for url in reversed(self.stack_list):
            print(url)


s = BrowserHistory()
s.visited("www.bloomberg.com")
s.visited("www.bh.com")
s.visited("www.google.com")
s.visited("www.bh.com")
s.showHistory()

'''
Time: O(1) for each method
Space: O(N), where N is the most URLs we save'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]

'''
It’s not difficult to realize that we need a stack so that back can be implemented. 
However, what to do for forward. 
Because you want the ability to visit all pages in the backward as well as the forward direction, we need to store the URLs whenever we go back. 
If you see the order in which we want to visit, you will quickly realize that we need two stacks. One to store history and another to store the next URLs in case we go back.

Two special cases:
You must always have at least one element in the history stack which is the page that you are currently at.
But for the forward stack, this condition is not necessary.

I am sure the following code will make it even clearer.
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]