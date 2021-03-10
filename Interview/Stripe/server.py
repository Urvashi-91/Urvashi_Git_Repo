'''
You're running a pool of servers where the servers are
numbered sequentially starting from 1. Over time, any
given server might explode, in which case its server
number is made available for reuse. When a new
server is launched, it should be given the lowest available number.

Write a function which, given the list of currently
allocated server numbers, returns the number of the next server to allocate.

For example, your function should behave something like the following:

>> next_server_number([5, 3, 1])
2
>> next_server_number([5, 4, 1, 2])
3
>> next_server_number([3, 2, 1])
4
>> next_server_number([2, 3])
1
>> next_server_number([])
1

Server names consist of an alphabetic host type (e.g. "apibox") concatenated with the server number,
with server numbers allocated as before (so "apibox1",
"apibox2", etc. are valid hostnames).

Write a name tracking class with two operations,
allocate(host_type) and deallocate(hostname).
The former should reserve and return the next
available hostname, while the latter should release
that hostname back into the pool.

# For example:
#
# >> tracker = Tracker.new()
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("apibox")
# "apibox2"
# >> tracker.deallocate("apibox1")
# nil
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("sitebox")
# "sitebox1"


'''
int
NextServerNumber(int[]
serversTaken){
    int
max = 0;
HashSet < int > possibles = new
HashSet < int > ();

foreach(int
currentServer in serversTaken){
if (currentServer > max)
{
// we
add
from max to

the
current
for (int i = max + 1; i < currentServer; i++){
                                             // add as a possible
possibles.Add(i);
}
max = currentServer;
}
if (possibles.Contains(currentServer))
possibles.Remove(currentServer);
}

if (possibles.Count > 0)
return possibles[0];

return max + 1;
}

'''
This question is asking the first missing positive integer from the list of n integers. (Total n-1 integers given and return 
value should be an integer missing (m) from this list. So, it is implied that 1<=m<=n.'''

#include<iostream>
#include<vector>
using namespace std;

  int missingInt(vector<int> v) {
	int cnt=0, tmp=v[0],n=v.size(),i=0;
	while(cnt<=n) {
			if(v[i] != i+1 && v[i]<=n) {
				tmp = v[v[i]-1];
				v[v[i]-1] = v[i];
				v[i]=tmp;
			}
			else i++;
			cnt++;
	}
	int j=0;
	for( j=0;j<n;++j)
		if(v[j]!=j+1) return j+1;
	return j+1;
}

int main() {
	vector<int> v = {4,1,5,3}; // Don't sort it. Otherwise it will be n log(n).
	int ret = missingInt(v);
	cout<<ret;
	return 0;
}

'''
We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative. We traverse the array again and print the first index which has positive value. In the following code, findMissingPositive() function does this part. Note that in findMissingPositive, we have subtracted 1 from the values as indexes start from 0 in C.'''

/ * Find
the
smallest
positive
missing
number
in an
array
that
contains
all
positive
integers * /
int
findMissingPositive(int
arr[], int
size)
{
int
i;

// Mark
arr[i] as visited
by
making
arr[arr[i] - 1]
negative.
// Note
that
1 is subtracted
because
index
start
// from

0 and positive
numbers
start
from

1
for (i = 0; i < size; i++)
    {
    if (abs(arr[i]) - 1 < size & & arr[abs(arr[i]) - 1] > 0)
    arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1];
    }

    // Return
    the
    first
    index
    value
    at
    which is positive
    for (i = 0; i < size; i++)
        if (arr[i] > 0)
            // 1 is added
            because
            indexes
            start
            from

            0
            return i + 1;

    return size + 1;
    }