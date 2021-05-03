'''
Method3: Bitwise XOR
TC: O(n)
SC: O(1)
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
'''
def find_single_number(arr):
  num = 0
  for i in arr:
      num ^= i
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()