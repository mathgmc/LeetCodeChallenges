# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        control = {}
        max_sub = 0
        left = right = 0

        while right < len(s):
            if s[right] not in control or control[s[right]]<left:
                control[s[right]] = right
                right+=1
                max_sub = max(max_sub, right - left)
            else:
                left = control[s[right]] + 1
                control[s[right]] = right
                right += 1
                max_sub = max(max_sub, right - left)
        
        return max_sub
                
            