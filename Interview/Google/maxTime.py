'''
You are given a string that represents time in the format hh:mm.
Some of the digits are blank (represented by ?).
Fill in ? such that the time represented by this string is the maximum possible.
Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example1:
Input: "?4:5?"
Output: "14:59"

Example2:
Input: "23:5?"
Output: "23:59"

Example3:
Input: "2?:22"
Output: "23:22"

Example4:
Input: "0?:??"
Output: "09:59"

Example5:
Input: "??:??"
Output: "23:59"
'''

# def maxTime(time):
#     if s[0] == "?":
#         if s[1] != "?":
#             if int(s[1]) > 3:
#                 s = "1" + s[1:]
#             else:
#                 s = "2" + s[1:]
#         else:
#             s = "2" + s[1:]
#     if s[1] == "?":
#         if (s[0] == "2"):
#             s = s[:1] + "3" + s[2:]
#         else:
#             s = s[:1] + "9" + s[2:]
#     if s[3] == "?":
#         s = s[:3] + "5" + s[4:]
#     if s[4] == "?":
#         s = s[:4] + "9"
#     return s

def maxTime(time):
    hh,mm = time.split(":")
    if hh == "??":
        hh = "23"
    else:
        for i in range(9,-1,-1):
            h = hh
            h = h.replace('?',str(i))
            if int(h) <= 23:
                hh = str(h)
                break

    if mm == "??":
        mm = "59"
    else:
        for j in range(9,-1,-1):
            m = mm
            m = m.replace('?',str(j))
            if int(m) <= 59:
                mm = str(m)
                break

    print (hh + ":" + mm)


maxTime("?4:5?")
maxTime("23:5?")
maxTime("2?:22")
maxTime("??:??")
maxTime("0?:??")
