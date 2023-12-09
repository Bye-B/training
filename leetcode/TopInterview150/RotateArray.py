class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        len_nums = len(nums)
        nums_return = nums
        nums = []
        for i in range(len_nums):
            
            print((len_nums+i-k) % len_nums)
            nums.append(nums_return[((len_nums+i-k) % len_nums)])
        nums_return = nums
        print(nums)
        return nums
    
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
            
            li += 1
            ri -= 1
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
nums = [1,2,3,4,5,6,7]
k = 3
my_solution = Solution()
print(my_solution.rotate(nums, k))