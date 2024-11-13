# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            max_profit = max(max_profit, ( p - buy_price ))

        
        return max_profit