# # A Naive Recursive Python program to count number of possible numbers
# # of given length
#
# # left, up, right, down move from current location
# row = [0, 0, -1, 0, 1]
# col = [0, -1, 0, 1, 0]
#
#
# # Returns count of numbers of length n starting from key position
# # (i, j) in a numeric keyboard.
# def getCountUtil(keypad, i, j, n):
#     if (keypad == None or n <= 0):
#         return 0
#
#     # From a given key, only one number is possible of length 1
#     if (n == 1):
#         return 1
#     k = 0
#     move = 0
#     ro = 0
#     co = 0
#     totalCount = 0
#
#     # move left, up, right, down from current location and if
#     # new location is valid, then get number count of length
#     # (n-1) from that new position and add in count obtained so far
#     for move in range(5):
#         ro = i + row[move]
#         co = j + col[move]
#         if (ro >= 0 and ro <= 3 and co >= 0 and co <= 2 and
#                 keypad[ro][co] != '*' and keypad[ro][co] != '#'):
#             totalCount += getCountUtil(keypad, ro, co, n - 1)
#     return totalCount
#
#
# # Return count of all possible numbers of length n
# # in a given numeric keyboard
# def getCount(keypad, n):
#     # Base cases
#     if (keypad == None or n <= 0):
#         return 0
#     if (n == 1):
#         return 10
#     i = 0
#     j = 0
#     totalCount = 0
#     for i in range(4):  # Loop on keypad row
#         for j in range(3):  # Loop on keypad column
#
#             # Process for 0 to 9 digits
#             if (keypad[i][j] != '*' and keypad[i][j] != '#'):
#                 # Get count when number is starting from key
#                 # position (i, j) and add in count obtained so far
#                 totalCount += getCountUtil(keypad, i, j, n)
#     return totalCount



# Driver code
keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]
# print("Count for numbers of length 1:", getCount(keypad, 1))
# print("Count for numbers of length 2:", getCount(keypad, 2))
# print("Count for numbers of length 3:", getCount(keypad, 3))
# print("Count for numbers of length 4:", getCount(keypad, 4))
# print("Count for numbers of length 5:", getCount(keypad, 5))

# This code is contributed by subhammahato348
def phoneDial(keypad, s):
    phone_dict = {}
    sum = len(s)
    for row in range(4):
        for col in range(3):
            phone_dict[keypad[row][col]] = (row,col)
    for i in range(len(s)-1):
        j = i+1
        if s[i] in phone_dict:
            x0 = (phone_dict[s[i]])[0]
            y0 = (phone_dict[s[i]])[1]
            x1 = (phone_dict[s[j]])[0]
            y1 = (phone_dict[s[j]])[1]

            sum += (x1-x0)+(y1-y0)


    print (sum)


phoneDial(keypad, '180')
