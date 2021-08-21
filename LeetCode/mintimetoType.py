import string
class Solution:
    def minTimeToType(self, word: str) -> int:
        """Keyboard list can have chars in any order"""
        keyboard=list(string.ascii_lowercase)
        # let us create a char map
        char_map = [-1] * 26
        for i, c in enumerate(keyboard):
            char_map[ord(c) - ord('a')] = i
        # calculate time
        t = 0
        prev_pos = 0
        for c in word:
            pos = char_map[ord(c) - ord('a')]
            t += (abs(pos  - prev_pos)+1) if abs(pos  - prev_pos)<abs(pos-prev_pos-26) else (abs(pos-prev_pos-26)+1)
            prev_pos = pos
        return t