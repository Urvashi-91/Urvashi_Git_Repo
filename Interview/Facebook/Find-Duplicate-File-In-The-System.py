'''
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Time complexity :
O(n∗x).
n strings of average length
x is parsed.

Space complexity :
O(n∗x).
map and
res size grows upto
n∗x.
'''


def findDuplicate(paths):
    hash_map = {}
    result = []
    for path in paths:
        path_split = path.split(' ')
        directory = path_split[0]
        for j in range(1, len(path_split)):
            content = path_split[j].split('(')
            file_path = directory + '/' + content[0]
            if content[1] not in hash_map:

                hash_map[content[1]] = [file_path]
            else:
                hash_map[content[1]].append(file_path)

    for value in hash_map.values():
        if len(value) > 1:
            result.append(value)
    return result

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
print(findDuplicate(paths))


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict = collections.defaultdict(list)
        res = list()

        for path in paths:
            parent_dir, *files = path.split(' ')
            for file in files:
                file_name, content = file.split('(')
                file_dict['(' + content].append(parent_dir + '/' + file_name)

        for k, v in file_dict.items():
            if len(v) > 1:
                res.append(v)

        return res