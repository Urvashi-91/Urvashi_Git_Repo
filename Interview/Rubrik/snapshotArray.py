from collections import defaultdict
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(dict)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[index][self.snap_id] = val

    def snap(self) -> int:
        res = self.snap_id
        self.snap_id += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        # get lastest snapshot before requested snap_id
        snaps = list(self.snaps[index])
        i = bisect.bisect(snaps, snap_id)
        if i > 0:
            snap_id_to_use = snaps[i - 1]
            return self.snaps[index][snap_id_to_use]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)