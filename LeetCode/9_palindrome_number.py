class Solution:
    def isPalindrome(self, x: int) -> bool:
        quocient = x
        result = 0

        if quocient < 0:
            return False

        while quocient > 0:
            digit = quocient % 10
            quocient = quocient // 10

            result = result * 10 + digit

        if result == x:
            return True
        else:
            return False
