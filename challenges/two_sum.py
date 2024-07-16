# Link: https://leetcode.com/problems/two-sum/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Difficulty: Easy
# Date: 2024-07-29

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_target = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in complement_target:
                return [complement_target[complement], i]

            complement_target[nums[i]]=i

        return []