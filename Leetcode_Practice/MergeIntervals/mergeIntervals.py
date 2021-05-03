'''
Method: Sort and merge
Time Complexity: O(nlognn)
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


'''
Method2: 
'''
from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sort the intervals on the start time
  intervals.sort(key=lambda x: x.start)

  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:  # overlapping intervals, adjust the 'end'
      end = max(interval.end, end)
    else:  # non-overlapping interval, add the previous internval and reset
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end

  # add the last interval
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()


main()




