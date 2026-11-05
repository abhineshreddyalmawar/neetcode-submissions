class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0 # initializing the left pointer to zero as buy day
        right =1 #initializing the right pointer to 1 as sell day
        best =0 # initializing the best=0 for max profit
        while right<len(prices):# 1<6:yes,2<6:yes,3<6:yes,4<6:yes,5<6:yes,6<6:no stops
            if prices[right]>prices[left]: # if 1>10 fails,5>1:yes,6>1:yes,7>1:yes,1>1:no
                profit= prices[right]-prices[left]# 5-1:4,6-1:5,7-1:6
                if profit>best:# 4>0:yes,5>4:yes,6>4:yes
                    best=profit # best =4,5,6
            else: left = right # left=1,5 skips for 5>1,6>1,7>1,
            right = right+1 # right= 2,3,4,5,6
        return best
print(Solution().maxProfit([10,1,5,6,7,1]))
print(Solution().maxProfit([10,8,7,5,2]))

        