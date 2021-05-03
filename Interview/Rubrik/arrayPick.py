'''
You are given 2 array with non-repeating numbers

Pick any number from array1
You can place the number at the start or end of the array2
Find the min operations required to convert second array to first one.
Can someone suggest ways to do it.

array 1 = 4,2,3,5,1,6
array 2 = 3,6,5,4,1,2

now we need to find the min ops required to convert array 2 to array 1. so
in first operation we pick no 4 from array2, so array 2 will be 4,3,6,5,1,2
in second operation we pick 2 from array2, so array 2 will be 4,2,3,6,5,1
in thrid operation we pick 6 from array2, array 2 will be 4,2,3,5,1,6

so min operation required will be 3
'''

def rearrange(arr1,arr2):
    temp = dict(zip(arr1,arr2))
    print(temp)
    start,curr_start, end,curr_end, longest = 0,0,0,0,0

    for key,value in temp:
        if key == value:
            curr_end += 1
        else:
            start += 1
            end += 1
            if longest < (end-start+1):
                end = curr_end
                start = curr_start
                longest = max((end-start+1),longest)
            else:







arr1 = [4, 2, 3, 1, 5, 6]
arr2 = [3, 1, 4, 6, 5, 2]
rearrange(arr1,arr2)