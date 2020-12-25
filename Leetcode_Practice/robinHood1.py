# from copy import deepcopy
#
#
# class TextEditor:
#
#     def __init__(self):
#         self.text = []
#         self.history = []
#         self.clipboard = []
#
#     def __repr__(self):
#         return ''.join(self.text)
#
#     def insert(self, text):
#         if text:
#             self.history.append(deepcopy(self.text))
#             self.text += list(text)
#
#     def delete(self):
#         if self.text:
#             self.history.append(deepcopy(self.text))
#             self.text.pop()
#
#     def copy(self, index):
#         if index < len(self.text):
#             self.clipboard = deepcopy(self.text[index:])
#
#     def paste(self):
#         if self.clipboard:
#             self.history.append(deepcopy(self.text))
#             self.text += deepcopy(self.clipboard)
#
#     def undo(self):
#         if self.history:
#             self.text = self.history.pop()
#
# def newTextEditor(operations):
#     editor = TextEditor()
#     text = ""
#     word = []
#     for k in operations:
#         word = k.split()
#         if "INSERT" in word:
#             editor.insert(word[1])
#         elif "COPY" in word:
#             editor.copy(int(word[1]))
#         elif "UNDO" in word:
#             editor.undo()
#         elif "PASTE" in word:
#             editor.paste()
#         elif "DELETE" in word:
#             editor.delete()
#         else:
#             continue
#
#     print(editor)
#
# operations = ["INSERT Da", "COPY 0", "UNDO", "PASTE", "PASTE", "COPY 2", "PASTE", "PASTE", "DELETE","DELETE", "INSERT aaam"]
# newTextEditor(operations)


# import collections
# def threeCharsDistinct(s):
#     n = len(s)
#     count,c,cnt = 0,0,0
#     for i in range(1,n-1):
#         l = [s[i-1],s[i],s[i+1]]
#         for items,count in collections.Counter(l).items():
#             if count == 1:
#                 c += 1
#         if c == 3:
#             cnt += 1
#             c = 0
#         else:
#             c = 0
#
#     print (cnt)
#
# s = "abcdaaae"
# threeCharsDistinct(s)



def prefixStrings(a,b):
    string = ""
    hash_dict = {}
    result = []
    for i in range(len(a)):
        string += a[i]
        hash_dict[i] = string
    for ele in b:
        if ele not in hash_dict.values():
            result.append(False)
        else:
            result.append(True)

    if False not in result:
        print ("true")
a = ["one","two","three"]
b = ["two","one"]
prefixStrings(a,b)