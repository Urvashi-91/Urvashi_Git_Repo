'''
Time Complexity #
The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

This sequence behavior tells us two things:

If the number
N
N is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
For
N
>
1
0
0
0
N>1000, suppose the number has ‘M’ digits and the next number is ‘N1’. From the above Wikipedia link, we know that the sum of the squares of the digits of ‘N’ is at most
9
2
M
9
​2
​​ M, or
8
1
M
81M (this will happen when all digits of ‘N’ are ‘9’).
This means:

N
1
<
8
1
M
N1<81M
As we know
M
=
l
o
g
(
N
+
1
)
M=log(N+1)
Therefore:
N
1
<
8
1
∗
l
o
g
(
N
+
1
)
N1<81∗log(N+1) =>
N
1
=
O
(
l
o
g
N
)
N1=O(logN)
This concludes that the above algorithm will have a time complexity of
O
(
l
o
g
N
)
O(logN).

Space Complexity #
The algorithm runs in constant space
O
(
1
)
O(1).
'''
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
