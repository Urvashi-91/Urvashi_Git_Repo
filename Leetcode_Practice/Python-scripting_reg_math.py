import re
import glob
re.match('./new/receipt-][0-9]*[24680].json','./new/receipt-2.json')
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') if re.match('/new/receipt-[0-9]*[24680].json', f)]
