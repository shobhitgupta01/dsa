class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        dict_w = {}

        # creating dict t
        for char in t:
            dict_t[char] = dict_t.get(char,0)+1
        
        i,j=0,0
        min_res = ""
        min_len = float('infinity')
        while j < len(s):
            dict_w[s[j]] = dict_w.get(s[j],0) + 1

            while all(dict_w.get(key, 0) >= value for key, value in dict_t.items()):
                if j-i+1 < min_len:
                    min_res = s[i:j+1]
                    min_len = j-i+1
                dict_w[s[i]] = dict_w.get(s[i])-1
                i+=1
            j+=1
        return min_res
            
            
sol = Solution()
res = sol.minWindow("ADOBECODEBANC", "ABC")
print(res)