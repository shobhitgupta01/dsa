# Scrambled String
# leetcode 87


class Solution:
    mp = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!= len(s2):
            return False
        
        if len(s1)==0 and len(s2)==0:
            return True
        
        if len(s1)==0 or len(s2)==0:
            return False

        if s1 == s2:
            return True

        # making key as concat of the two strings
        key = s1+s2
        if key in Solution.mp:
            return Solution.mp[key]
        
        for i in range(1,len(s1)):
            swapped = self.isScramble(s1[0:i], s2[len(s2)-i:]) and  self.isScramble(s1[i:], s2[0:len(s2)-i])

            non_swapped = self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:])

            if swapped or non_swapped:
                Solution.mp[key] = True
                return Solution.mp[key]
        
        Solution.mp[key] = False
        return Solution.mp[key]
        

print(Solution().isScramble('great', 'eatrg'))