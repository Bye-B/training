class Solution(object):
    def lengthOfLastWord(self, s):
            in_word = False
            len_current_word = 0
            for i in range(len(s)):
                  if s[i].isalpha() == True:
                        if in_word == False:
                              in_word = True
                              len_current_word = 0
                        len_current_word += 1
                  else:
                        in_word = False
            return len_current_word

my_string = "last word"
my_solution = Solution()
print(my_solution.lengthOfLastWord(my_string))