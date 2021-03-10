'''
using globbing to read files that match a pattern --> usd only for file names
shutil is a high level file operations
'''

import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print ("'processed' directory already exist")

receipts = glob.glob('./new/receipt-[0-9]*.json')  #return filenames
subtotal = 0.0
for path in receipts:
    with open(path) as f:
        content = json.load(f) #dump is for witeout, load takes readable file object and returns json object
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    destination = f"./processed/{name}"
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")
print("Receipt subtotal: %.2f" % subtotal)