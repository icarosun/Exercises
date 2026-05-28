class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**(31) - 1
        INT_MIN = 2**(31)

        sign = -1 if x < 0 else 1
        num = abs(x)
        quocient = num
        result = 0

        while (quocient > 0):
            rest = quocient % 10
            quocient = quocient // 10
            
            result = result * 10 + rest
            
            if (result > INT_MAX or result > INT_MIN):
                return 0

        return sign * result 
