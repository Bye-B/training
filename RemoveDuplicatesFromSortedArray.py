class Solution(object):
    def removeDuplicates(self, nums):
        number_duplicates = 0
        deleted = False
        for i in range(1,len(nums)):
            if deleted == True:
                i -= 1
                deleted = False
            if i < len(nums):
                if nums[i-1] == nums[i]:
                    del nums[i]
                    deleted = True
                    number_duplicates += 1 
            else:
                return number_duplicates
        return number_duplicates
    
    def removeDuplicates2(self, nums):
        number_duplicates = 1
        for i in range(1,len(nums)):
                if nums[i-1] != nums[i]:
                    nums[number_duplicates] = nums[i]
                    number_duplicates += 1 
        return number_duplicates
nums =[1,1,1,2]
my_solution = Solution()
print(my_solution.removeDuplicates(nums))