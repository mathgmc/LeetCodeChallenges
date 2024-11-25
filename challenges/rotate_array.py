# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		r = k % n
		if r > 0:
			rotated = nums[-r:] + nums[:-r]
			for i in range(n):
				nums[i] = rotated[i]
