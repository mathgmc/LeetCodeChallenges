# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        i = 0
        start = 0
        letter_stack = {}
        
        while i < len(s):
            if s[i] in letter_stack:
                max_count = max(count, max_count)
                count = 0
                letter_stack = {}
                start +=1
                i = start
            else:
                count +=1
                letter_stack[s[i]] = True
                i+=1
        
        return max(max_count, count)

class Solution1: # Best solution
    def lengthOfLongestSubstring(self, s):
        left = max_length = 0
        last_seen = {}
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            max_length = max(max_length, right - left + 1)
            last_seen[c] = right
        return max_length