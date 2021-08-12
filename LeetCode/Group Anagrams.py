class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []
        if len(strs) == 0:
            return []
        dic = {} # using this to keep a log o feach and every unique word
        for s in strs:
            key = ''.join(sorted(s)) #checking for anagrams
            if key in dic:
                dic[key].append(s) #appending the value of the key unique word with the anagram set
            else:
                dic[key] = [s] # new key value pair
        return list(dic.values()) #returning the values of the dictionary