'''
Generate test data using random package
JSON package to
'''

import random
import json
import os

count = int(os.getenv("File_COUNT") or 100) #build 100 random files or as specified while executing file
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f"./new/receipt-{identifier}.json", 'w')