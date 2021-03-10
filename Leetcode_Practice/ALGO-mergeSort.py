import array
def mergeSortSolutions(arr):
    temp = []
    mergeSort(arr,temp, 0,len(arr)-1)
    return arr

def mergeSort(arr, temp, leftStart, rightEnd):
    if (leftStart >= rightEnd):
        return None
    else:
        pivot = (leftStart + rightEnd) / 2
        mergeSort(arr, temp, leftStart, pivot)
        mergeSort(arr, temp, pivot+1, rightEnd)
        mergeHalves(arr,temp,leftStart,rightEnd)
    return arr


def mergeHalves(arr, temp, leftStart ,  rightEnd):
    leftEnd = rightEnd + leftStart / 2
    rightStart = leftEnd + 1
    index = leftStart

    while (leftStart <= leftEnd and rightStart <= rightEnd):
        if arr[leftStart] <= arr[rightStart]:
            temp[index] = arr[leftStart]
            index += 1
            leftStart += 1
        else:
            temp[index] = arr[rightStart]
            index += 1
            rightStart += 1
    temp[index:leftEnd] = arr[leftStart:leftEnd].copy()
    temp[index:rightEnd] = arr[rightStart:rightEnd].copy()
    arr[index:rightEnd] = temp[leftStart:rightEnd].copy()
    return arr





print(mergeSortSolutions([10,5,2,7,4,9,12,1,8,6,11,3]))