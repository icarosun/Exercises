import re

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1

        indice = 0
        size_string = len(s)
        result = 0

        while ((indice < size_string) and (s[indice] == " ")):
            indice += 1

        if (indice < size_string):
            if (s[indice] == "-"):
                sign = -1
                indice += 1
            elif (s[indice] == "+"):
                indice += 1

        while indice < size_string and s[indice].isdigit():
            digit = int(s[indice])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            
            indice += 1
        
        return result * sign
