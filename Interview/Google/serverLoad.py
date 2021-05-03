'''
There are some processes that need to be executed. Amount of a load that process causes
on a server that runs it, is being represented by a single integer.
Total load caused on a server is the sum of the loads of all the processes that run on that server.
You have at your disposal two servers, on which mentioned processes can be run.
Your goal is to distribute given processes between those two servers in the way that,
absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes,
return the minimum absolute difference of server loads.


Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively,
and the difference of their loads will be equal to 1.
'''
'''
Method1: Top-Down Approach
TC: O(NS)
SC: )(NS)
'''
def server_load(proc):
    s = sum(proc)
    n = len(proc)
    dp = [[-1 for y in range(s+1)]for x in range(n)]
    return server_load_recursive(dp,proc,0,0,0)

def server_load_recursive(dp,proc,curr_idx,sum1,sum2):
    n = len(proc)
    s = sum(proc)
    if curr_idx >= n:
        return abs(sum1-sum2)

    if dp[curr_idx][sum1] == -1:
        diff1 = server_load_recursive(dp,proc,curr_idx+1,sum1+proc[curr_idx],sum2)
        diff2 = server_load_recursive(dp, proc, curr_idx + 1, sum1, sum2+proc[curr_idx])
        dp[curr_idx][sum1] = min(diff1,diff2)
    return dp[curr_idx][sum1]


print(server_load([1,2,3,4,5]))
print(server_load([10,10,9,9,2]))
print(server_load([]))
print(server_load([1]))

'''
Method2:Bottom-Up Approach
TC: O(NS)
SC: O(NS)
'''

def serverload(proc):
    sum = sum(proc)
    n = len(proc)
    dp = [[False for x in range(int(sum/2)+1)]for y in range(n)]

    for x in range(n):
        dp[x][0] = True
    for y in range(int(sum/2)+1):
        if proc[0] == dp[0][y]:
            dp[0][y] = True

    for x in range(n):
        for y in range(int(sum/2)+1):
            if dp[x][y] == False:
                if proc[x] <= y:
                    dp[x][y] = dp[x-1][y-proc[x]]
                elif dp[x-1][y]:
                    dp[x][y] = dp[x-1][y]

    sum1=0
    for y in range(int(sum/2)+1,-1,-1):
        if dp[n-1][y]:
            sum1 = y
            break
    sum2 = sum-sum1
    return abs(sum1-sum2)



