class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        output = [0]
        memory = set()
        S = list(S)
        while S:
            memory.add(S.pop(0))
            output[-1] += 1
            if not memory.intersection(set(S)) and S:
                output.append(0)
        return output


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        Start = End = 0
        result = []
        for i, c in enumerate(S):
            End = max(End, last[c])
            if i == End:
                result.append(End - Start + 1)
                Start = i + 1
        return result
