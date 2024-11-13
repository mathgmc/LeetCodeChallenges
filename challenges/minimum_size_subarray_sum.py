# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub = len(nums)+1
        left = right = 0
        aux=0

        while left < len(nums) and right < len(nums):
            aux += nums[right]
            right += 1
            if aux >= target:
                while aux >= target:
                    min_sub = min(min_sub, (right-left))
                    aux -= nums[left]
                    left += 1
                        
        return min_sub if min_sub != len(nums)+1 else 0
