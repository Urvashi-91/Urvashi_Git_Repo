def max_profit(prices):
    high = max(prices.values())
    low = min(prices.values())
    cities = []
    i = 0
    for city,value in prices.items():
        if value == low:
            cities.insert(0, city)
        elif value == high:
            cities.insert(1, city)
    print (cities)




#TestCase1
prices = {'London': 72, 'Neq York': 70, 'Miami': 67, 'Tokyo': 60}
max_profit(prices)

#testCase2:
prices = {'London': 72, 'Neq York': 70, 'Miami': 60, 'Tokyo': 60}

