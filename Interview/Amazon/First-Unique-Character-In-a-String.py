'''
First Non-repeating character
TC: O(N)
SC: O(1)
'''
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)
        for key, value in enumerate(s_dict):
            if s_dict[value] == 1:
                return key
        return -1


'''
First repeating character
'''
def firstrepeatingChar(s):
    s_dict = Counter(s)
    for key, value in enumerate(s_dict):
        if s_dict[value] > 1:
            return key
    return -1

print (firstrepeatingChar('geeksforgeeks'))


# Python program to find the first
# repeated character in a string
def firstRepeatedChar(str):
    h = {}  # Create empty hash

    # Traverse each characters in string
    # in lower case order
    for ch in str:

        # If character is already present
        # in hash, return char
        if ch in h:
            return ch;

        # Add ch to hash
        else:
            h[ch] = 0

    return '\0'


# Driver code
print(firstRepeatedChar("geeksforgeeks"))