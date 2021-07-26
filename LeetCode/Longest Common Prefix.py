class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            if len(set([s[i] for s in strs])) != 1:
                return strs[0][:i]
        return strs[0][:min_len]