import math
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        minimal_number_of_same_digits = math.floor(len(nums)/2)
        start = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if (i-1) - start >= minimal_number_of_same_digits:
                    return nums[i-1]
                start = i


    def majorityElement2(self, nums):
        nums.sort()
        middle_element = len(nums)//2
        return nums[middle_element]
       
nums = [1,1,1,2,1,4]
my_solution = Solution()
print(my_solution.majorityElement(nums))