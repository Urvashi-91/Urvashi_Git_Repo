class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        #4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]



class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue

            #2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []

        return ans