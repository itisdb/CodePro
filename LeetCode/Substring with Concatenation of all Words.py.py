import collections

class Solution(object):
    def findSubstring(self, s, words):
        if not words: return []
        
        wc = len(words) #word count
        wl = len(words[0]) #word length
        ans = []
        
        i = 0
        j = wc*wl
        
        countExpected = collections.Counter(words)
        
        while j<=len(s):
            if self.test(s[i:j], wl, countExpected): ans.append(i)
            i += 1
            j += 1
        
        return ans
    
    
    def test(self, s, wl, countExpected):
        counter = collections.Counter() #{word:how many time the word is used}
        i = 0
        
        while i<len(s):
            word = s[i:i+wl]
            if word not in countExpected or counter[word]>=countExpected[word]: return False
            i += wl
            counter[word] += 1
            
        return True