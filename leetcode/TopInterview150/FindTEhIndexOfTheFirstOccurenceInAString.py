class Solution(object):
    def strStr(self, haystack, needle):
            current_state_needle = ""
            for i in range(len(haystack)):
                  if haystack[i] == needle[0]:
                        if i + len(needle)<= len(haystack):
                              for j in range(len(needle)):
                                    if haystack[i+j] == needle[j]:
                                          current_state_needle += needle[j]
                                    if current_state_needle == needle:
                                          return i
                              current_state_needle = ""
                        else:
                              return -1

            return -1

haystack = "sadbutsad"
needle = "sad"
my_solution = Solution()
print(my_solution.strStr(haystack, needle))