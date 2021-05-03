class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans = []
        # 1) For each word w, For loop w[:i]
        # 2) check if the front segment[0:j] is in wordSet and if the [j+1: i] is in the wordset
        # EDGE CASE: cats is in wordSet but not concatenated, catsdog is in wordSet but also concatenated
        # SOLUTION to edge case: instead of storing True/False, store the concatenated time, base is 1, and 2 means it is
        # concatenated with "" + word, which is the word itself
        # 3) If yes:w[:i] is concatenated=> dp[-1] > 2, append to ans, BREAK(to pass the edge case full of "a")

        for i, w in enumerate(words):
            dp = [0] * (len(w) + 1)
            dp[0] = 1
            for i in range(1, len(w) + 1):
                for j in range(i):
                    if dp[j] and w[j: i] in wordSet:
                        dp[i] = max(dp[i], dp[j] + 1)
                        if dp[i] > 2:
                            break
            if dp[-1] > 2:
                ans.append(w)
        return ans


def find_word_concatenation(str1, words):
  if len(words) == 0 or len(words[0]) == 0:
    return []

  word_frequency = {}

  for word in words:
    if word not in word_frequency:
      word_frequency[word] = 0
    word_frequency[word] += 1

  result_indices = []
  words_count = len(words)
  word_length = len(words[0])

  for i in range((len(str1) - words_count * word_length)+1):
    words_seen = {}
    for j in range(0, words_count):
      next_word_index = i + j * word_length
      # Get the next word from the string
      word = str1[next_word_index: next_word_index + word_length]
      if word not in word_frequency:  # Break if we don't need this word
        break

      # Add the word to the 'words_seen' map
      if word not in words_seen:
        words_seen[word] = 0
      words_seen[word] += 1

      # No need to process further if the word has higher frequency than required
      if words_seen[word] > word_frequency.get(word, 0):
        break

      if j + 1 == words_count:  # Store index if we have found all the words
        result_indices.append(i)

  return result_indices


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
