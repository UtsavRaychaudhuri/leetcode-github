class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hashmap=[]
        # def maxprofit(i):
        #     mp=0
        #     minprice=prices[i]
        #     for j in range(i,len(prices)):
        #         minprice=min(prices[j],minprice)
        #         mp=max(mp,prices[j]-minprice)
        #     return mp
        # mp=0
        # for i in range(len(prices)):
        #     hashmap.append(maxprofit(i))
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if j==len(prices)-1:
        #             mp=max(prices[j]-prices[i],mp)
        #             continue
        #         mp=max(prices[j]-prices[i]+hashmap[j+1],mp)
        # return mp
        buy1,sell1,buy2,sell2=sys.maxsize,0,sys.maxsize,0
        for i in range(len(prices)):
            buy1=min(buy1,prices[i])
            sell1=max(sell1,prices[i]-buy1)
            buy2=min(buy2,prices[i]-sell1)
            sell2=max(sell2,prices[i]-buy2)
        return sell2