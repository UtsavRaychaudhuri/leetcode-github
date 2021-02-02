class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy,sell=[sys.maxsize]*(k+1),[0]*(k+1)
        for i in range(len(prices)):
            for j in range(1,len(buy)):
                buy[j]=min(buy[j],prices[i]-sell[j-1])
                sell[j]=max(sell[j],prices[i]-buy[j])
        return sell[k]
        