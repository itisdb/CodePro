class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        word_len = len(words[0])
        word_num = len(words)
        result = []
        for i in range(len(s) - word_len * word_num + 1):
            cur_word_num = 0
            cur_word_dict = {}
            for j in range(word_num):
                cur_word = s[i + j * word_len: i + (j + 1) * word_len]
                if cur_word in words:
                    cur_word_num += 1
                    cur_word_dict[cur_word] = cur_word_dict.get(cur_word, 0) + 1
                    if cur_word_dict[cur_word] > words.count(cur_word):
                        break
                else:
                    break
            if cur_word_num == word_num:
                result.append(i)
        return result
        