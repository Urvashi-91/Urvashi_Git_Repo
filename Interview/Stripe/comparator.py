'''
Implement a comparator class that is capable of sorting by multiple key: order pairs, each pair being a tiebraker for the previous
'''

void
MergeSort < T > (T[] array, params Func < T, IComparable >[] conditions)
{
if (conditions.Length == 0)
conditions = new
Func < T, IComparable > []
{
    (x) = > x as IComparable
};
MergeSort(array, 0, array.Length - 1, conditions);
}

void
MergeSort < T > (T[] array, int start, int end, Func < T, IComparable >[] conditions)
{
    int
mid = (start + end) / 2;

// partition / Sort
each
part
if (start < mid)
MergeSort(array, start, mid, conditions);

if (mid + 1 < end)
MergeSort(array, mid + 1, end, conditions);

// Merge
Merge(array, start, mid, end, conditions)
}

void
Merge(T[]
array, int
start, int
mid, int
end, Func < T, IComparable > []
conditions){
    int
chunkLength = end - start + 1;
T[]
auxArray = new
T[chunkLength];

int
idxLeft = start;
int
idxRight = mid + 1;

// fill
the
aux
array
for (int i = 0; i < chunkLength; i++){
if (idxLeft > mid) {
// take right
auxArray[i] = array[idxRight++];
}
else if (idxRight > end) {
// take left
auxArray[i] = array[idxLeft++];
}
else if (Compare(array[idxLeft], array[idxRight]) > 0){
// take left
auxArray[i] = array[idxLeft++];
}
else {
// take right
auxArray[i] = array[idxRight++];
}
}

// override the original array
for (int i = 0; i < chunkLength; i++){
array[i+start] = auxArray[i];
}
}

int
Compare < T > (T t1, T t2, Func < T, IComparable >[] conditions)
{
for (int i = 0; i < conditions.Length; i++){
    IComparable v1 = conditions[i](t1);
IComparable v2 = conditions[i](t2);

if (v1 != null & & v2 != null){
int value = v1.CompareTo(v2);

if (value != 0)
return value;
}
}
return 0;
}