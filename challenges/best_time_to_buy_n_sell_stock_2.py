# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = None
        sell = None

        for i in range(len(prices)):
            if buy is None or buy > prices[i]:
                buy = prices[i]
            else:
                sell = prices[i]
            
            if sell is not None and (i == len(prices) - 1 or prices[i + 1] < sell):
                profit += sell - buy
                buy = None
                sell = None
        
        return profit

