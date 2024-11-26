# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        control = {}
        mapped_t = set()
        for i in range(len(s)):
            if s[i] not in control:
                if t[i] in mapped_t:
                    return False
                control[s[i]] = t[i]
                mapped_t.add(t[i])
            elif t[i] != control[s[i]]:
                return False
        return True