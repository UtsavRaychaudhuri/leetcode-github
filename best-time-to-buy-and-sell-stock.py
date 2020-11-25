class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice, highest = float('inf'), 0
        for price in prices:
            if price < minPrice: minPrice = price
            elif price - minPrice > highest:
                highest = price - minPrice
        return highest
        
