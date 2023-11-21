class Solution(object):
    def maxProfit(self, prices):
      profit = 0
      left = 0
      right = 1
      for i in range(len(prices)):
            current = prices[i]
            rest = prices[i:]
            rest.sort()
            if rest[-1]-current > profit:
                  profit = rest[-1]-current
      return profit
      def maxProfit2(self,prices):
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit



nums = [7,1,5,3,6,4]
my_solution = Solution()
print(my_solution.maxProfit(nums))