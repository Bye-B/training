class Solution(object):
      def canJump(self, nums):
            
            joker = 0
            length = len(nums)
            if length <=1:
                  return True
            current_outer_position = 0
            while True:
                  current_position = current_outer_position
                  if current_outer_position + nums[current_outer_position] < length:
                        print("injoker")
                        if current_outer_position + nums[current_outer_position] > joker and (nums[current_outer_position + nums[current_outer_position]])/2!=0:
                              joker = (current_outer_position + nums[current_outer_position])/2
                              print("hä")
                  print(current_position)
                  print("joker:")
                  print(joker)
                  while True:
                        if current_position == length or current_position + nums[current_position]+1>=length:
                              return True
                        if nums[current_position + nums[current_position]] != 0:
                              current_position += nums[current_position]

                        elif nums[current_position] != 0:
                              current_position += 1
                        else:
                              break
                  check_moved = current_outer_position
                  for i in range(1,nums[current_outer_position]):
                        if nums[current_outer_position + i] != 0:
                              current_outer_position += i
                              break
                  
                  if check_moved == current_outer_position:
                        if joker > current_outer_position:
                              print("joker used")
                              current_outer_position = joker
                        else:
                              return False


nums = [5,9,3,2,1,0,2,3,3,1,0,0]
my_solution = Solution()
print(my_solution.canJump(nums))