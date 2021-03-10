my_file = open("../Interview/Stripe/sone_file.txt", 'w+') #r: read, w:write, r+:read + write, 'w+: write and read, x: create, a:append, r+t:read and get text back, r+b: read and get byte data
my_file.write('beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops \n',
    'Bishops \n',
    'Nightcrawler \n'
])
#my_file.seek(0) #to move cursor back to 0 as at the moment the cursor stays where it is on the last position until you have closed it
my_file.close()
my_file = open("../Interview/Stripe/sone_file.txt", 'r')
print(my_file.read())
my_file.close()


'''with open'''


with open('../Interview/Stripe/xmen.txt', 'w+') as my_file:
    my_file.write('beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops \n',
        'Bishops \n',
        'Nightcrawler \n'
    ])

    for line in my_file.readlines():
        print(line)