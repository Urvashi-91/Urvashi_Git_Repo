<<<<<<< HEAD
def maxKoccurences(sequence, words):
    sol = []
    for word in words:
        r = 0
        N = len(word)
        m = 0
        i = 0
        while i<len(sequence) - N +1:
            if sequence[i:i+N] == word:
                m+=1
                r = max(r, m)
                i +=N
            else:
                m = 0
                i+=1
        sol.append(r)
    print (sol)
=======
def maxKoccurences(sequence, words):
    sol = []
    for word in words:
        r = 0
        N = len(word)
        m = 0
        i = 0
        while i<len(sequence) - N +1:
            if sequence[i:i+N] == word:
                m+=1
                r = max(r, m)
                i +=N
            else:
                m = 0
                i+=1
        sol.append(r)
    print (sol)
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
maxKoccurences(("ababcbabc"), ["ab","babc","bca"])