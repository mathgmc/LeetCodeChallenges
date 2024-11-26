# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_control = {}

        for c in magazine:
            if c in mag_control:
                mag_control[c] += 1
            else:
                mag_control[c] = 1
            
        for c in ransomNote:
            if c not in mag_control or mag_control[c] <= 0:
                return False
            mag_control[c] -= 1
        
        return True    
