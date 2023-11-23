class Solution(object):
      def romanToInt(self, s):
            einer = 0
            zehner = 0
            hunderter = 0
            tausender = 0
            while len(s)!= 0:
                  if "IV" in s:
                        einer = 4
                        s = s.replace("IV","")
                  if "IX" in s:
                        einer = 9
                        s = s.replace("IX","")
                  if "XL" in s:
                        zehner = 40
                        s = s.replace("XL","")
                  if "CL" in s:
                        zehner = 90
                        s = s.replace("CL","")
                  if "CD" in s:
                        hunderter = 400
                        s = s.replace("CD","")
                  if "CM" in s:
                        hunderter = 900
                        s = s.replace("CM","")
                  if "I" in s[0]:
                        einer += 1
                        s = s[1:]
                  if "V" in s[0]:
                        einer += 5
                        s = s[1:]
                  if "X" in s[0]:
                        zehner += 10
                        s = s[1:]
                  if "L" in s[0]: 
                        zehner += 50
                        s = s[1:]
                  if "C" in s[0]:
                        hunderter += 100
                        s = s[1:]
                  if "D" in s[0]:
                        hunderter += 500
                        s = s[1:]
                  if "M" in s[0]:
                        tausender += 1000
                        s = s[1:]
            return tausender + hunderter + zehner + einer

      def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans


roman = "III"
my_solution = Solution()
print(my_solution.romanToInt(roman))