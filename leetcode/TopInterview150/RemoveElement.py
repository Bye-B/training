class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        
        return k

nums =[1,2,1,1,2]
val = 2
my_solution = Solution()
print(my_solution.removeElement(nums, val))