<<<<<<< HEAD
# from collections import defaultdict
# import math
# def digitAnagrams(a):
#     count = 0
#     dict = defaultdict(list)
#     for i in range(len(a)):
#         s="".join(sorted(str(a[i])))
#         dict[s].append(a[i])
#         
#     for k in dict:
#         n = len(dict[k])
#         if n>= 2:
#             pair = math.factorial(n) // (2*(math.factorial(n-2)))
#             count += pair
#     print (count)
# 
# a = [25,35,872,228,53,278,872]
# digitAnagrams(a)


# def stringAnagrams(s1, s2):
#     if (sorted(s1) == sorted(s2)):
#         print ("Anagrams")
#     else:
#         print ("Not Anagrams")
#         
# s1 = "listen"
# s2 = "silent"
# stringAnagrams(s1, s2)

# from collections import defaultdict
#
# def printAnagramsTogether(words):
#     groupedWords = defaultdict(list)
#
#     # Put all anagram words together in a dictionary
#     # where key is sorted word
#     for word in words:
#         groupedWords["".join(sorted(word))].append(word)
#
#     # Print all anagrams together
#     for group in groupedWords.values():
#         print(" ".join(group))
#
#
# if __name__ == "__main__":
#     arr =  ["cat", "dog", "tac", "god", "act"]
#     printAnagramsTogether(arr)
=======
# from collections import defaultdict
# import math
# def digitAnagrams(a):
#     count = 0
#     dict = defaultdict(list)
#     for i in range(len(a)):
#         s="".join(sorted(str(a[i])))
#         dict[s].append(a[i])
#         
#     for k in dict:
#         n = len(dict[k])
#         if n>= 2:
#             pair = math.factorial(n) // (2*(math.factorial(n-2)))
#             count += pair
#     print (count)
# 
# a = [25,35,872,228,53,278,872]
# digitAnagrams(a)


# def stringAnagrams(s1, s2):
#     if (sorted(s1) == sorted(s2)):
#         print ("Anagrams")
#     else:
#         print ("Not Anagrams")
#         
# s1 = "listen"
# s2 = "silent"
# stringAnagrams(s1, s2)

from collections import defaultdict  
  
def printAnagramsTogether(words): 
    groupedWords = defaultdict(list) 
  
    # Put all anagram words together in a dictionary  
    # where key is sorted word 
    for word in words: 
        groupedWords["".join(sorted(word))].append(word) 
  
    # Print all anagrams together 
    for group in groupedWords.values(): 
        print(" ".join(group))       
  
  
if __name__ == "__main__":    
    arr =  ["cat", "dog", "tac", "god", "act"]   
    printAnagramsTogether(arr) 
>>>>>>> 6a511d70a9044aa21ff457120200837581634c3b
