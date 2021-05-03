'''This question was given to me during a phone interview from a hot bay area startup:
Rubrik. It goes something like this
If:
Company A owns 10% of Company B,
Company B owns 5% of Company C,
Company B owns 5% of Company D,
Company A owns 2% of Company C

then, how much of Company C does A own? 2.5%'''

# company ownerships
from collections import defaultdict


def get_ownership(ownlist, source, target):
    '''
    ownlist = example [(A, B, 10), (A, C, 5) ....]
    source = example A
    target = example C
    '''
    visited = set()
    adj_map = defaultdict(dict)
    for edge in ownlist:
        u, v, w = edge
        adj_map[u][v] = w * 1.0 / 100.0

    # print adj_map
    def visit(source):
        for v in adj_map[source].keys():
            if v not in visited:
                visit(v)
        for j in adj_map[source].keys():
            if j != v and j in adj_map[v]:
                adj_map[source][j] += adj_map[source][v] * adj_map[v][j]
        visited.add(source)
        #print("from source={} adj_map {}".format(source, adj_map))

    visit(source)

    if source in visited:
        return adj_map[source].get(target, 0)


print (get_ownership([('A', 'B', 10.0), ('A', 'C', 2.0), ('B', 'C', 5.0), ('B', 'D', 2.0)], 'A', 'C') ) # ans 0.025
print (get_ownership([('A', 'B', 10.0), ('A', 'C', 2.0), ('B', 'C', 5.0), ('B', 'D', 2.0)], 'A', 'D') ) # ans 0
print (get_ownership([('A', 'B', 10.0), ('A', 'C', 2.0), ('B', 'C', 5.0), ('B', 'D', 2.0), ('D', 'C', 50.0)],'A', 'C') ) # ans 0.026