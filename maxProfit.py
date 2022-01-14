class Solution:
    def maxProfit(self, prices):
        

        profit = 0
        
        min_price = prices[0]
        max_price = prices[0]

        for j in range(1,len(prices)):    

            if prices[j] > max_price:
                max_price = prices[j]
            if prices[j] < min_price:
                min_price = prices[j]
                max_price = prices[j]
            if max_price - min_price > profit:
                   profit = max_price - min_price

        return profit

                
sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))