# Link: https://leetcode.com/problems/two-sum/
# Link2: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

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
    

class Solution2: # Best solution
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) -1

        while r > l:
            actual_sum = numbers[l] + numbers[r]
            if actual_sum == target:
                return [l+1, r+1]
            
            if actual_sum > target:
                r -= 1
            else:
                l += 1

        return ["Houston", "We have a problem"] # This should never happen because there should always be a solution
