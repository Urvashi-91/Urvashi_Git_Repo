# stock_prices = {} #Dictionary and [] is LIST
# with open("stock_prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices[day] = price
# print (stock_prices['9-Mar'])

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range (self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        print (h % self.MAX)
t = HashTable()
t.get_hash('march 6')