class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right=1
        best =0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit= prices[right]-prices[left]
                if profit>best:
                    best=profit
            else:
                left=right
            right=right+1
        return best
print(Solution().maxProfit([10,1,5,6,7,1]))
print(Solution().maxProfit([10,8,7,5,2]))

        