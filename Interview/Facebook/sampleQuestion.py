'''
"Coding Sample question:
# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces."
'''
'''
Solution:
facebook -->{f:1, a:1, c:1, e:1, b:1, o:2, k:1}
coffee kebab --> {c:1, o:1, f:2, e:3, k:1, b:2, a:1}
facebook - cofee kebab --> {f:-1, a:0, c:0, e:-2, k:0, }
count_facebook - count_word / count_facebook = count
'''
from collections import Counter
def get_num_stickers(words):
    logo = Counter('facebook')
    word_list = words.split(" ")
    total = Counter()
    for word in word_list:
        word_count = Counter(word)
        total += word_count
    total.subtract(logo)
    return 1+max(total.values())

print (get_num_stickers('coffee kebab'))
print (get_num_stickers('book'))
print (get_num_stickers('ffacebook'))

