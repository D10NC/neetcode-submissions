class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]
        profit = 0 # profit = sell price - buy price

        for i in prices:
            todayProfit = i - buyPrice
            if todayProfit > profit:
                profit = todayProfit
            
            if i < buyPrice:
                buyPrice = i
        
        return profit
