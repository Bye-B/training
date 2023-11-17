class Solution(object):
      def merge1(self, nums1, m, nums2, n):
            max_nums1 = nums1[m-1]
            print(max_nums1)
            position_n = 0
            if n == 0:
                  pass
            else:
                  for i in range(0,m+n):
                        if position_n < n:
                              if nums2[position_n] < nums1[i] or nums2[position_n]> max_nums1 and max_nums1 != nums1[i]:
                                    nums1.insert(i, nums2[position_n])
                                    position_n += 1
                  nums1 = nums1[:m+n]
            print(nums1)
      def merge2(self, nums1, m, nums2, n):
            for j in range(n):
                  nums1[m+j]=nums2[j]
            nums1.sort()      

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
my_solution = Solution()
my_solution.merge2(nums1, m, nums2, n)
