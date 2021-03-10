'''Throughout this interview, we'll write code to analyze a simple server uptime log. These logs are much simplified,
and are just strings of space separated 0's and 1's. The log is a string of binary digits (e.g. "0 0 1 0").
Each digit corresponds to 1 hour of the server running:'''

'''
"1" = , "down" // server crashed during the hour
"0" = <didn't crash>, "up" // server did not crash during the hour

EXAMPLE: A server with log "0 0 1 0" ran for 4 hours and crashed during hour #3
hour: |1|2|3|4|
log : |0|0|1|0|
^
|
down during hour #3
We can permanently remove a server at the beginning of any hour during its operation. A server is on the network until 
it is removed. Note that a server stays POWERED ON after removal, it's just not on the network.

EXAMPLE: Remove a server with log "0 0 1 0"

hour :  | 1 | 2 | 3 | 4 |
log  :  | 0 | 0 | 1 | 0 |
remove_at: 0 1 2 3 4 // remove_at being x means "server removed before hour x+1"
^ ^
| |
before hour #1 after hour #4

We'd like to understand the best times to remove a server. So let's introduce an aggregate metric called a "penalty" 
for removing a server at a bad time.

We define our penalty like this:
+1 penalty for each DOWN hour when a server is on the network
+1 penalty for each UP hour after a server has been removed

Further Examples:

EXAMPLE:

hour : 1 2 3 4 // total penalty = 3 (3 server-up hours after remove)
log : 0 0 1 0
^
|
remove_at = 0

hour : 1 2 3 4 // total penalty = 1 (1 server-down hour before remove)
log : 0 0 1 0
^
|
remove_at = 4'''

''' TASK 1a)
Write a function: compute_penalty, that computes the total penalty, given
a server log (as a string) AND a time at which we removed the server from the network (call that variable remove_at)
Note that for a server log of length n hours, the remove_at variable can range from 0, meaning "before the first hour" to n, 
meaning "after the final hour".'''
def computer_penalty(server_log:str, remove_at:int) -> int:
    #server_log = list(server_log)
    n_hours = len(server_log)
    if remove_at == 0:
        return server_log.count("0")
        #number of zeroes is penalty

    elif remove_at == n_hours:
        return server_log.count("1")
        #number of ones is penalty
    else:
        return server_log[:remove_at].count("1") + server_log[remove_at:].count("0")


print("Test Cases for 1a")
log = "0010"
remove_at_1 = 0
remove_at_2 = 3
print (computer_penalty(log, remove_at_1))
print (computer_penalty(log, remove_at_2))


'''TASK 1b)
Use your answer for compute_penalty to write another function: find_best_removal_time, that returns
the best remove_at hour, given a server log.'''

def find_best_removal_time(server_log:str):
    to_remove = []
    for i in range (len(server_log)+1):
        to_remove.append(computer_penalty(server_log, i))
    return [idx for idx, num in enumerate(to_remove) if num == min(to_remove)]
    #return [to_remove.index(min(to_remove)), to_remove]
print("The best remove_at hour is ", find_best_removal_time(log))


'''TASK 2a)
Now that we're able to analyze single server logs, let's analyze some aggregate logs.
Aggregate logs are text files that contain lots of logs. The files contain only BEGIN, END,
1, 0, spaces and newlines. We'll only consider inner BEGINs and ENDs to be valid log sequences.

Put another way, any sequence of 0s and 1s surrounded by BEGIN and END forms a valid
sequence. For example, the sequence "BEGIN BEGIN BEGIN 1 1 BEGIN 0 0 END 1 1 END" has
only one valid sequence "BEGIN 0 0 END".

Write a function, get_best_removal_times, that takes a file name as a parameter, and
returns an array of best removal hours for every valid server log in that file.'''

import re
def get_best_removal_times(file):
    i = 1
    listOfBestRemovalTime = []
    with open(file, "r") as log_file:
        for line in log_file.readlines():
            if line == "\n":
                continue
            else:

                line1 = re.sub(r"\s+", "", line)
                valid = re.findall("BEGIN[0-1]*END", line1)
                for v in valid:
                    v = v.replace("BEGIN","")
                    v = v.replace("END","")
                    print(f"Best removal time for {i} server log is: {find_best_removal_time(v)}")
                    listOfBestRemovalTime.append(find_best_removal_time(v))
                    i += 1
    return listOfBestRemovalTime
print (get_best_removal_times("server_log"))
