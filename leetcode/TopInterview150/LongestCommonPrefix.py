class Solution(object):
    def longestCommonPrefix(self, s):
            common_prefix = ""
            index_of_same_prefix = 0
            len_shortest_word = 201
            for i in range(len(s)):
                  if len(s[i]) < len_shortest_word:
                        len_shortest_word = len(s[i])
            for i in range(len_shortest_word):
                  for j in range(len(s)):
                        if s[j][i] != s[0][i]:
                              return common_prefix
                  common_prefix += s[0][index_of_same_prefix]
                  index_of_same_prefix += 1

            return common_prefix

strs = ["flower","flow","flight"]
my_solution = Solution()
print(my_solution.longestCommonPrefix(strs))