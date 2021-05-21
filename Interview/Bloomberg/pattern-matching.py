'''
https://www.techiedelight.com/wildcard-pattern-matching/
'''
# Function that matches the input string with a given wildcard pattern
def isMatching(str, pattern, n, m, lookup):
    # If both the input string and pattern reach their end,
    # return true
    if m < 0 and n < 0:
        return True

    # If only the pattern reaches its end, return false
    elif m < 0:
        return False

    # If only the input string reaches its end, return true
    # if the remaining characters in the pattern are all `*`
    elif n < 0:
        for i in range(m + 1):
            if pattern[i] != '*':
                return False
        return True

    # If the subproblem is encountered for the first time
    if not lookup[n][m]:
        if pattern[m] == '*':
            # 1. `*` matches with current characters in the input string.
            # Here, we will move to the next character in the string.

            # 2. Ignore `*` and move to the next character in the pattern
            lookup[n][m] = isMatching(str, pattern, n - 1, m, lookup) or \
                           isMatching(str, pattern, n, m - 1, lookup)
        else:
            # If the current character is not a wildcard character, it
            # should match the current character in the input string
            if pattern[m] != '?' and pattern[m] != str[n]:
                lookup[n][m] = False
            # check if `pattern[0…m-1]` matches `str[0…n-1]`
            else:
                lookup[n][m] = isMatching(str, pattern, n - 1, m - 1, lookup)

    return lookup[n][m]


# Wildcard Pattern Matching Implementation in Python
if __name__ == '__main__':

    str = "xyxzzxy"
    pattern = "x***x?"

    # create a DP lookup table
    lookup = [[False for x in range(len(pattern) + 1)] for y in range(len(str) + 1)]

    if isMatching(str, pattern, len(str) - 1, len(pattern) - 1, lookup):
        print("Match")
    else:
        print("No Match")