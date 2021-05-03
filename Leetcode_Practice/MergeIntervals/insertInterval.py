'''
Method1: Insert and Sort and Merge
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            else:
                output.append([start, end])
        return output

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)
'''
Method2: Insert at each comparison
TC:
SC:

'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        N = len(intervals)
        idx = 0
        output = []
        newStart, newEnd = newInterval

        # case1: append output until intervals[i][0] <= newStart
        while idx < N and intervals[idx][0] <= newStart:
            output.append(intervals[idx])
            idx += 1
        # case2: append newInterval or Merge newInterval
        if not output:
            output.append(newInterval)
        elif output[-1][1] < newStart:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newEnd)
        print(output, idx)

        # case3: append or merge rest of the intervals
        while idx < N:
            newStart, newEnd = intervals[idx]
            if output[-1][1] < newStart:
                output.append([newStart, newEnd])
            else:
                output[-1][1] = max(output[-1][1], newEnd)
            idx += 1

        return output


'''
Method3: Same as Method2
TC:O(N)
SC:O(N)
SC:
'''
def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip (and add to output) all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1

  # insert the new_interval
  merged.append(new_interval)

  # add all the remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
