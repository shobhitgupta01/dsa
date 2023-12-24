from typing import List

class Solution:
    def getKey(self, string):
        res= [0]*26
        for char in string:
            key = ord(char) - ord('a')
            res[key]+=1
        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for string in strs:
            key = self.getKey(string)
            anagram_map[key] = anagram_map.get(key,[]) + [string]
        
        return anagram_map.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))