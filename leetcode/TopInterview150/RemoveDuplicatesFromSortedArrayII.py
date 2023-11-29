class Solution(object):
      def removeDuplicates1(self, nums):
            return_nums = []
            if len(nums)<2:
                  return len(nums)
            for i in range(len(nums)):
                  if nums[i] != nums [i-2]:
                        return_nums.append(nums[i])
            return len(return_nums)

      def removeDuplicates(self, nums):
        k = 0
        
        for i in nums:
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k

nums = [1,1,1,2,2,3]
my_solution = Solution()
print(my_solution.removeDuplicates(nums))