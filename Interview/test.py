
def A(activity):
    login_TS = logout_TS = difference = 0
    result = []
    for record in activity:
        if record[1] == '@login':
            login_TS = record[0]
        elif record[1] == '@logout':
            logout_TS = record[0]

            difference = abs(logout_TS - login_TS)

            result.append(difference)
    return sum(result)

def B(activity):
    result = []
    client = []
    for record in activity:
        if record[1] == '@startVideo':
            if client:
                startTS = record[0]
                client.append(record[2])

            else:
                client.append(record[2])


        elif record[1] == '@stopVideo':
            if record[2] in client and len(client) >= 2:
                stopTS = record[0]
                difference = abs(stopTS - startTS)
                client.remove(record[2])
                result.append(difference)


            else:
                client.remove(record[2])
        else:

            continue
    return sum(result)

activity = [(1, '@login', None),
(5, '@startVideo', 'Bob'),
(20, '@startVideo', 'Thomas'),
(66, '@stopVideo', 'Thomas'),
(70, '@startVideo', 'Lily'),
(75, '@stopVideo', 'Bob'),
(78, '@stopVideo', 'Lily'),
(100, '@logout', None),
(150, '@login', None),
(160, '@startVideo', 'Thomas'),
(205, '@stopVideo', 'Thomas'),
(210, '@logout', None) ]

print(A(activity))
print(B(activity))