class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        last = prices[0]
        for i in range(len(prices)):
            if prices[i]<last:
                last = prices[i]
            if prices[i]>last:
                profit += prices[i]-last
                last = prices[i]
        return profit

prices = [7,1,5,3,6,4]
my_solution = Solution()
print(my_solution.maxProfit(prices))