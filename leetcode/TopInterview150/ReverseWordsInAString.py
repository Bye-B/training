class Solution(object):

      def reverseWords(self, s):
            s = s.strip()
            length = len(s)
            reversed = ""
            current_word = ""
            for i in range(1,length+1):
                  if s[length-i] == " " or length-i == 0:
                        if i == length :
                              current_word += s[length-i]
                        current_word = current_word[::-1]
                        current_word = current_word.strip()
                        if current_word == " ":
                              print("*")
                              current_word = ""
                        
                        reversed += current_word
                        reversed = reversed.strip()
                        reversed += " "
                        current_word = ""
                  else:
                        current_word += s[length-i]
            
            reversed = reversed.strip()
            return reversed

s = "the sky is     blue   "

my_solution = Solution()
print(my_solution.reverseWords(s))