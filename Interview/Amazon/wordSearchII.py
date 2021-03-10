class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = {}

    def search(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '#' in curr_node

    def startsWith(self, prefix):
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return True


class Solution:
    def __init__(self):
        self.root = Trie()

    def findWords(self, board, words):
        t = Trie()
        for word in words:
            t.insert(word)

        m = len(board)
        n = len(board[0])
        output = []

        def dfs(row, col, path):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == None:
                return

            t_path = path + [board[row][col]]
            str_path = "".join(t_path)

            if not t.startsWith(str_path):
                return

            elif t.search(str_path) and str_path not in output:
                output.append(str_path)

            placeholder = board[row][col]
            board[row][col] = None
            dfs(row - 1, col, t_path)
            dfs(row + 1, col, t_path)
            dfs(row, col - 1, t_path)
            dfs(row, col + 1, t_path)
            board[row][col] = placeholder

        for r in range(m):
            for c in range(n):
                dfs(r, c, [])
        return output


sol = Solution()
print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))
