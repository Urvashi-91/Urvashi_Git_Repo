class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+"
        s = list(s)

        def operate(presign, stack, num):
            if presign == '+':
                stack.append(num)
            elif presign == '-':
                stack.append(-num)
            elif presign == '*':
                stack.append(stack.pop() * num)
            elif presign == '/':
                stack.append(math.trunc(stack.pop() / num))

        def dfs(i):
            stack = []
            num = 0
            presign = "+"
            while i < len(s):
                if s[i] == '(':
                    s[i] = ''
                    num, i = dfs(i + 1)
                elif s[i] == ')':
                    s[i] = ''
                    operate(presign, stack, num)
                    return sum(stack), i
                elif s[i].isnumeric():
                    num = 10 * num + int(s[i])
                    s[i] = ''
                elif s[i] in "+-*/":
                    operate(presign, stack, num)
                    presign = s[i]
                    num = 0
                    s[i] = ''
                i += 1
            return sum(stack)

        return dfs(0)
