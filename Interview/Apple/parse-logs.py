'''
Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages in sorted time order.
'''
import re
from collections import Counter
path = '/Users/hanu/Documents/Urvashi_Git_Repo/Interview/Apple/messages'
regexp = '^(.*? \d+ \d+\:\d+).*'
regexp1 = '^(.*? \d+ \d+\:\d+)\:\d+ .*? (.*?)\: .*'
minute = []
minute1 = []
with open(path) as f:
    data = f.readlines()
    for line in data:
        minute.append(re.match(regexp, line).groups())
        minute1.append(re.match(regexp1, line).groups())

    print(dict(Counter(minute)))
    print(dict(Counter(minute1)))


